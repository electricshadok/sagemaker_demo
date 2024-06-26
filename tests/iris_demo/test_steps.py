import os

import numpy as np

from ml_pipeline.iris_demo.steps.data.download import Download
from ml_pipeline.iris_demo.steps.data.process import Process
from ml_pipeline.iris_demo.steps.deployment.deploy_sklearn import DeploySKLearn
from ml_pipeline.iris_demo.steps.deployment.onnx_inference import ONNXInference
from ml_pipeline.iris_demo.steps.model.evaluate_classifier import EvaluateClassifier
from ml_pipeline.iris_demo.steps.model.train_classifier import TrainClassifier


def test(
    raw_dir: str = "./tests/data/raw",
    train_dir: str = "./tests/data/processed/train",
    test_dir: str = "./tests/data/processed/test",
    models_dir: str = "./tests/training/models",
    artifacts_dir: str = "./tests/training/artifacts/",
):
    download_step = Download(output_dir=raw_dir)
    download_step()

    process_step = Process(input_dir=raw_dir, output_train_dir=train_dir, output_test_dir=test_dir, test_ratio=0.2, seed=42)
    process_step()

    train_step = TrainClassifier(train_dir=train_dir, models_dir=models_dir, artifacts_dir=artifacts_dir, seed=42)
    train_step()

    evaluate_step = EvaluateClassifier(test_dir=test_dir, models_dir=models_dir)
    evaluate_step()

    deploy_step = DeploySKLearn(models_dir=models_dir)
    deploy_step()

    onnx_path = os.path.join(models_dir, "model.onnx")
    inference_step = ONNXInference(onnx_path)
    input_data = np.array([[5.1, 3.5, 1.4, 0.2]])
    result = inference_step(input_data)
    print(result)


if __name__ == "__main__":
    test()
