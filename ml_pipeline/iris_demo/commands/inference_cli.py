"""
Inference CLI

Syntax:
    python inference_cli.py
        --model_path ./training/models/model.onnx
"""

import numpy as np

from ml_pipeline.cli_builder import CLIBuilder
from ml_pipeline.iris_demo.steps.deployment.onnx_inference import ONNXInference


def main():
    builder = CLIBuilder(cls=ONNXInference, description="Inference CLI")
    cli = builder.get_cli()
    input_data = np.array([[5.1, 3.5, 1.4, 0.2]])
    cli(input_data)
    # builder.show_example_command("inference_cli.py")


if __name__ == "__main__":
    main()
