class SageMakerConfig:
    def __init__(
        self,
        account_id: str,
        region: str = "us-east-2",
        role_name: str = "SageMakerExecutionRole",
        image_repo_name: str = "ai_pipe",
        image_tag: str = "latest",
        bucket_name: str = "aipipe",
    ):
        self.account_id = account_id
        self.region = region
        self.role_name = role_name
        self.image_repo_name = image_repo_name
        self.image_tag = image_tag
        self.bucket_name = bucket_name

    @property
    def role_arn(self):
        return f"arn:aws:iam::{self.account_id}:role/{self.role_name}"

    @property
    def image_uri(self):
        return f"{self.account_id}.dkr.ecr.{self.region}.amazonaws.com/{self.image_repo_name}:{self.image_tag}"

    @property
    def bucket_arn(self):
        return f"arn:aws:s3:::{self.bucket_name}"

    def __str__(self):
        return (
            f"Configuration for AWS SageMaker:\n"
            f"Region: {self.region}\n"
            f"AWS Account ID: {self.account_id}\n"
            f"Role ARN: {self.role_arn}\n"
            f"Docker Image URI: {self.image_uri}\n"
            f"S3 Bucket: {self.bucket_name}\n"
            f"S3 Bucket ARN: {self.bucket_arn}"
        )
