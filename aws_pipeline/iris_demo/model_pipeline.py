import sagemaker
from sagemaker.estimator import Estimator
from sagemaker.inputs import TrainingInput
from sagemaker.workflow.steps import ProcessingStep, TrainingStep

from aws_pipeline.sagemakerconfig import SageMakerConfig


def get_model_steps(config: SageMakerConfig, processing_step: ProcessingStep):
    estimator = Estimator(
        image_uri=config.image_uri,  # Reuse the same image URI if it has your training environment
        role=config.role_arn,  # IAM role ARN
        instance_count=1,  # Number of instances to use for training
        instance_type="ml.m4.xlarge",  # Instance type for training, you can choose the same or a different one based on your training needs
        output_path=f"s3://{config.bucket_name}/model_output",  # Specify where to save the model artifacts
        sagemaker_session=sagemaker.Session(),  # Session to use (TODO : is that needed ?)
    )
    # Note: the env variable SM_MODEL_DIR is set to estimator.output_path

    # Specify your training script located within your source directory
    estimator.entry_point = "train_cli.py"
    estimator.source_dir = "ml_pipeline/iris_demo/commands/"

    estimator.set_hyperparameters(seed=0)

    s3_train_dir = f"s3://{config.bucket_name}/processed_data/train"
    if processing_step:
        s3_train_dir = processing_step.properties.ProcessingOutputConfig.Outputs["processing_out"].S3Output.S3Uri

    training_step = TrainingStep(
        name="TrainingStep",
        estimator=estimator,
        inputs={
            # Note: the env varibale SM_CHANNEL_TRAIN is set to s3_processed_dir
            # Note: validation data could be added here
            "train": TrainingInput(
                s3_data=s3_train_dir,
                content_type="csv",
            )
        },
    )
    return training_step

    """ TODO : Add model validation
    Model Validation
    """

    """ TODO : Add Model Registry
        # Optionally, add a model registration step to register the trained model in SageMaker Model Registry
    model_register = RegisterModel(
        name="RegisterModel",
        estimator=estimator,
        content_types=["application/json"],  # Example content type
        response_types=["application/json"],
        inference_instances=["ml.t2.medium", "ml.m5.large"],
        transform_instances=["ml.m5.large"],
        model_package_group_name="YourModelPackageGroupName"
    )
    """
