"""
Download dataset CLI

Syntax:
    python download_cli.py --output_dir ./data/raw
"""

from ml_pipeline.cli_builder import CLIBuilder
from ml_pipeline.iris_demo.steps.data.download import Download


def main():
    builder = CLIBuilder(cls=Download, description="Download CLI")
    cli = builder.get_cli()
    cli()
    # builder.show_example_command("download_cli.py")


if __name__ == "__main__":
    main()
