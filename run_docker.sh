#!/bin/bash

# Set variables
IMAGE_NAME="ai_pipe"
TAG="latest"
DOCKERFILE_PATH="./Dockerfile"

# Run the Docker image in python mode
# The container is automatically removed after it stops (--rm)
#docker run -it --rm $IMAGE_NAME:$TAG

# Run the Docke image in bash mode
# The container is automatically removed after it stops (--rm)
docker run -it --rm $IMAGE_NAME:$TAG bash
