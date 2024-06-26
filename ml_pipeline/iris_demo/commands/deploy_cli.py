"""
Deploy CLI

Syntax:
    python deploy_cli.py
        --models_dir ./training/models
"""

from ml_pipeline.cli_builder import CLIBuilder
from ml_pipeline.iris_demo.steps.deployment.deploy_sklearn import DeploySKLearn


def main():
    builder = CLIBuilder(cls=DeploySKLearn, description="Deploy CLI")
    cli = builder.get_cli()
    cli()
    # builder.show_example_command("deploy_cli.py")


if __name__ == "__main__":
    main()
