# Sagemaker Demo

Simple machine learning pipeline using AWS Sagemaker.

## Prerequisites

- Docker
- AWS CLI configured with necessary permissions


## Setup Instructions

### Check Docker Status

Run `docker info`. If it fails, start Docker:

```
open -a Docker
```

### Build and Push Docker Image to AWS ECR

```
./build_and_push_docker.sh 
```

### Set Up and Update ML Pipeline

```
python aws_pipeline/iris_demo/pipeline_setup.py --update --no-start
```


## Tests

### Test Individual Steps
```
python tests/iris_demo/test_steps.py
```

### Test Commands
```
./tests/iris_demo/test_commands.sh
```

### Test AWS Pipeline Creation
```
python tests/iris_demo/test_aws_pipeline.py
```


## TODO

- [ ] Add training, evaluation, and deployment steps in the AWS pipeline.
- [ ] Run AWS pipeline locally: [AWS blog on ML workflows with SageMaker Pipelines](https://aws.amazon.com/blogs/machine-learning/best-practices-and-design-patterns-for-building-machine-learning-workflows-with-amazon-sagemaker-pipelines/).
- [ ] Add parameters to the AWS pipeline.
- [ ] Complete the `/docs` section.
- [ ] Add a deep learning project with MLflow.
- [ ] Implement GitHub Actions to run `ruff`.
