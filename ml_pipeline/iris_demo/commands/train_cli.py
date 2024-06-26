"""
Training CLI

Syntax:
    python train_cli.py
        --train_dir ./data/processed/train
        --models_dir ./training/models
        --artifacts_dir ./training/artifacts
        --seed 0
"""

import os

from ml_pipeline.cli_builder import CLIBuilder
from ml_pipeline.iris_demo.steps.model.train_classifier import TrainClassifier


def main():
    # Note: For AWS training variable environment
    # check https://sagemaker.readthedocs.io/en/stable/overview.html
    models_dir, train_dir = None, None
    if "SM_MODEL_DIR" in os.environ:
        models_dir = os.environ["SM_MODEL_DIR"]
    if "SM_CHANNEL_TRAIN" in os.environ:
        train_dir = os.environ["SM_CHANNEL_TRAIN"]
    cloud_run = models_dir and train_dir

    if cloud_run:
        # cloud execution
        builder = CLIBuilder(cls=TrainClassifier, description="Training CLI", models_dir=models_dir, train_dir=train_dir)
    else:
        # cloud execution
        builder = CLIBuilder(cls=TrainClassifier, description="Training CLI")

    cli = builder.get_cli()
    cli()
    # builder.show_example_command("train_cli.py")


if __name__ == "__main__":
    main()
