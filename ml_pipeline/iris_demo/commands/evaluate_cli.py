"""
Evaluation CLI

Syntax:
    python evaluate_cli.py
        --test_dir ./data/processed/test
        --models_dir ./training/models
"""

from ml_pipeline.cli_builder import CLIBuilder
from ml_pipeline.iris_demo.steps.model.evaluate_classifier import EvaluateClassifier


def main():
    builder = CLIBuilder(cls=EvaluateClassifier, description="Evaluation CLI")
    cli = builder.get_cli()
    cli()
    # builder.show_example_command("evaluate_cli.py")


if __name__ == "__main__":
    main()
