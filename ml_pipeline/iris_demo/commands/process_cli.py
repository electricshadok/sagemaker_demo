"""
Process CLI

Syntax:
    python process_cli.py
        --input_dir ./data/raw
        --output_train_dir ./data/processed/train
        --output_test_dir ./data/processed/test
        --test_ratio 0.2
        --seed 0
"""

from ml_pipeline.cli_builder import CLIBuilder
from ml_pipeline.iris_demo.steps.data.process import Process


def main():
    builder = CLIBuilder(cls=Process, description="Process CLI")
    cli = builder.get_cli()
    cli()
    # builder.show_example_command("process_cli.py")


if __name__ == "__main__":
    main()
