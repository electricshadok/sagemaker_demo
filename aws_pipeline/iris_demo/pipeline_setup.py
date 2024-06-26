import argparse
import json

import sagemaker
from sagemaker.processing import ScriptProcessor
from sagemaker.workflow.pipeline import Pipeline

from aws_pipeline import helpers
from aws_pipeline.iris_demo.data_pipeline import get_data_steps
from aws_pipeline.iris_demo.model_pipeline import get_model_steps
from aws_pipeline.sagemakerconfig import SageMakerConfig


def sagemaker_config() -> SageMakerConfig:
    """Get SageMaker configuration."""
    config = SageMakerConfig(
        account_id=helpers.get_account_id(),
        region=helpers.get_region(),
        role_name="SageMakerExecutionRole",
        image_repo_name="ai_pipe",
        image_tag="latest",
        bucket_name="aipipe",
    )
    return config


def build_sagemaker_pipeline(
    config: SageMakerConfig,
    data_pipeline: bool = True,
    model_pipeline: bool = True,
) -> Pipeline:
    """Build and return a SageMaker pipeline."""
    processor = ScriptProcessor(
        command=["python3"],
        image_uri=config.image_uri,
        role=config.role_arn,
        instance_count=1,
        instance_type="ml.t3.medium",
    )
    steps = []

    processing_step = None
    if data_pipeline:
        download_step, processing_step = get_data_steps(config, processor)
        steps.extend([download_step, processing_step])

    if model_pipeline:
        training_step = get_model_steps(config, processing_step)
        steps.extend([training_step])

    pipeline = Pipeline(
        name="Pipeline",
        steps=steps,
        sagemaker_session=sagemaker.Session(),
    )
    return pipeline


def export_sagemaker_pipeline(pipeline: Pipeline, pipeline_path: str = "pipeline_definition.json"):
    """Export the pipeline definition to a JSON file."""
    pipeline_def = pipeline.definition()
    pipeline_json = json.dumps(pipeline_def, indent=4)
    with open(pipeline_path, "w") as f:
        f.write(pipeline_json)


def pipeline_to_cloud(role_arn: str, pipeline: Pipeline, update: bool = True, start: bool = False):
    """Update or start the pipeline in the cloud."""
    if update:
        # Add/Update the pipeline configuration in the cloud.
        pipeline.upsert(
            role_arn=role_arn,
            description="pipeline demo",
            tags=[
                {"Key": "Project", "Value": "Demo Project"},
                {"Key": "Owner", "Value": "Data Science Team"},
            ],
        )

    if start:
        # You can check the log in Amazon CloudWatch and the progress in SagemakerStudio
        execution = pipeline.start()
        print(f"Execution ARN: {execution.arn}")
        status = execution.describe()["PipelineExecutionStatus"]
        print(f"Status of the pipeline execution: {status}")


def pipeline_setup(data_pipeline: bool = True, model_pipeline: bool = True, update: bool = True, start: bool = False):
    config = sagemaker_config()
    print(config)
    pipeline = build_sagemaker_pipeline(config, data_pipeline, model_pipeline)
    pipeline_to_cloud(config.role_arn, pipeline, update, start)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SageMaker pipeline setup")
    parser.add_argument("--update", default=True, action=argparse.BooleanOptionalAction, help="Update the pipeline in SageMaker")
    parser.add_argument("--start", default=False, action=argparse.BooleanOptionalAction, help="Start the pipeline execution")
    args = parser.parse_args()

    pipeline_setup(data_pipeline=True, model_pipeline=True, update=args.update, start=args.start)
