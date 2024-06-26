from sagemaker.processing import ProcessingInput, ProcessingOutput, Processor
from sagemaker.workflow.steps import ProcessingStep

from aws_pipeline.sagemakerconfig import SageMakerConfig


def get_data_steps(config: SageMakerConfig, processor: Processor):
    # Note: For both ProcessingInput and ProcessingOutput, the path in the processing container must begin with /opt/ml/processing/
    local_raw_dir = "/opt/ml/processing/raw/"
    local_processed_dir = "/opt/ml/processing/processed/"
    local_processed_train_dir = f"{local_processed_dir}/train/"
    local_processed_test_dir = f"{local_processed_dir}/test/"
    s3_raw_dir = f"s3://{config.bucket_name}/raw_data"
    s3_processed_dir = f"s3://{config.bucket_name}/processed_data"

    # Download Step
    download_step = ProcessingStep(
        name="DownloadStep",
        processor=processor,
        inputs=[],  # No input
        outputs=[
            ProcessingOutput(
                source=local_raw_dir,
                destination=s3_raw_dir,
                output_name="download_out",
            )
        ],
        # Arguments passed to the script
        job_arguments=["--output_dir", local_raw_dir],
        code="ml_pipeline/iris_demo/commands/download_cli.py",
    )

    # Processing Step
    processing_step = ProcessingStep(
        name="ProcessingStep",
        processor=processor,
        inputs=[
            ProcessingInput(
                source=download_step.properties.ProcessingOutputConfig.Outputs["download_out"].S3Output.S3Uri,
                destination=local_raw_dir,
                input_name="processing_in",
            )
        ],
        outputs=[
            ProcessingOutput(
                source=local_processed_dir,
                destination=s3_processed_dir,
                output_name="processing_out",
            )
        ],
        # Arguments passed to the script
        # Note: list of strings (including numerical values)
        job_arguments=[
            "--input_dir",
            local_raw_dir,
            "--output_train_dir",
            local_processed_train_dir,
            "--output_test_dir",
            local_processed_test_dir,
            "--test_ratio",
            "0.2",
            "--seed",
            "0",
        ],
        code="ml_pipeline/iris_demo/commands/process_cli.py",
    )

    return download_step, processing_step
