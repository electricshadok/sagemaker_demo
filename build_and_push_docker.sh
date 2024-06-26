#!/bin/bash

# Prerequisites:
# - User must be logged in to the AWS CLI with appropriate credentials.
# - Ensure that the AWS CLI is configured with credentials that have permissions to access Amazon ECR.
#   This includes permissions for `ecr:GetLoginPassword`, `ecr:DescribeRepositories`, `ecr:CreateRepository`, and `ecr:PutImage`.
# - Check your AWS CLI configuration using `aws configure list` to ensure that it is correctly set up.
# This script builds a Docker image, tags it, and pushes it to an AWS ECR repository.

# Variables
IMAGE_NAME="ai_pipe"            # Name of the Docker image.
TAG="latest"                    # Tag for the Docker image.
DOCKERFILE_PATH="./Dockerfile"  # Path to the Dockerfile.

REPOSITORY_NAME=$IMAGE_NAME     # Name of the repository in AWS ECR.
REGION="us-east-2"              # AWS region where the ECR repository is located.

# Retrieve AWS account ID dynamically from AWS STS
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query "Account" --output text)
if [ -z "$AWS_ACCOUNT_ID" ]; then
    echo "Failed to retrieve AWS account ID. Ensure you are logged in correctly."
    exit 1
fi

 # Base URL for ECR repository
ECR_BASE_URL="$AWS_ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com"

# Build the Docker image locally.
docker build -t "$IMAGE_NAME:$TAG" -f "$DOCKERFILE_PATH"  --platform "linux/amd64" .

# Authenticate the Docker client to the AWS ECR registry.
# This command retrieves a temporary password using AWS credentials and uses it to log the Docker client into the ECR repository.
# It ensures that subsequent Docker operations on the ECR repository (like push and pull) are authorized.
aws ecr get-login-password --region "$REGION" | docker login --username AWS --password-stdin $ECR_BASE_URL

# Check if the ECR repository exists, create if it does not.
if aws ecr describe-repositories --repository-names "$REPOSITORY_NAME" --region "$REGION" > /dev/null 2>&1; then
    echo "Repository '$REPOSITORY_NAME' exists in region $REGION."
else
    echo "Repository '$REPOSITORY_NAME' does not exist in region $REGION."
    # Optionally create the repository if it does not exist:
    # aws ecr create-repository --repository-name "$REPOSITORY_NAME" --region "$REGION"
    # echo "Repository '$REPOSITORY_NAME' created in region $REGION."
    exit 1  # Exit if repository does not exist and is not created.
fi

# Tag the Docker image with the full ECR repository URI.
docker tag "$IMAGE_NAME:$TAG" "$ECR_BASE_URL/$REPOSITORY_NAME:$TAG"

# Push the Docker image to the ECR repository.
docker push "$ECR_BASE_URL/$REPOSITORY_NAME:$TAG"

