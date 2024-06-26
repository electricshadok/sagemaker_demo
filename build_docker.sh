#!/bin/bash

# Set variables
IMAGE_NAME="ai_pipe"
TAG="latest"
DOCKERFILE_PATH="./Dockerfile"

# Build the Docker image
docker build -t "$IMAGE_NAME:$TAG" -f "$DOCKERFILE_PATH"  --platform "linux/amd64" .
