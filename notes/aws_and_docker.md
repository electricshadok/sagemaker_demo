# AWS and Docker


## Build Docker image (locally)
Containerize your things.
Copy the pipeline and the source code in docker

TODO

## Build Docker image (on AWS)

TODO

## Push Docker images to (Amazon ECR)

Amazon Elastic Container Registry (Amazon ECR) is an AWS managed container image registry.

### Step 0 : AWS Credentials

Make sure your AWS CLI is configured with the correct credentials and permissions. You can check which profile is currently configured with:

```
aws configure list
```

### Step 1 : Create an ECR Repository

If you don't have a ECR repository with AWS account do the following
1. **Open the AWS Management Console** and go to the Elastic Container Registry service.
2. **Create a new repository:**
    - Click “Create repository”.
    - Name your repository (e.g., ai_pipe).
    - Keep the default settings or configure them as needed, then create the repository.

### Step 2 : Authenticate Docker to your ECR Repository with the CLI

See : https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html


```
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com
```

Replace `<your-region>` and `<your-aws-account-id>` with your actual AWS region and account ID.

You can get those two using the 

```
echo "Region:"
aws configure get region

echo "Account ID:"
aws sts get-caller-identity --query "Account" --output text
```

**Important about region** : When using Amazon Elastic Container Registry (ECR), it's possible to have your Docker image repository in a different AWS region from your default AWS configuration or other AWS services !
