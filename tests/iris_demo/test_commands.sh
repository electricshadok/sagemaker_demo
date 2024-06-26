#!/bin/bash

# Run the pipeline using command lines
python ml_pipeline/iris_demo/commands/download_cli.py
python ml_pipeline/iris_demo/commands/process_cli.py
python ml_pipeline/iris_demo/commands/train_cli.py
python ml_pipeline/iris_demo/commands/evaluate_cli.py
python ml_pipeline/iris_demo/commands/deploy_cli.py
python ml_pipeline/iris_demo/commands/inference_cli.py
