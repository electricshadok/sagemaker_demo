# AWS Setup

1. Create a role for sagemaker
2. Create ECR repository
3. Create S3 Bucket for storage

##  Create an IAM Role for SageMaker

- in IAM Management Console
- Click Roles on the sidebar, then click Create role.
- Attach policies that will grant the necessary permissions for SageMaker. Common policies include:
- AmazonSageMakerFullAccess – Provides full access to SageMaker resources.
- AmazonS3FullAccess – (Or more restricted permissions to specific S3 buckets if needed for storing input data, output data, and model artifacts).
- AmazonEC2ContainerRegistryFullAccess – If you are using custom Docker images hosted in ECR.

...

## Create ECR Repository

...


## 