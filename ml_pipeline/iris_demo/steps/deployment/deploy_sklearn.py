import os

import joblib
import onnx
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

from ml_pipeline.iris_demo.constants import MODEL_FILENAME, MODEL_ONNX, MODELS_DIR


class DeploySKLearn:
    def __init__(self, models_dir: str = MODELS_DIR):
        self.models_dir = models_dir

    def __call__(self):
        model_path = os.path.join(self.models_dir, MODEL_FILENAME)
        onnx_path = os.path.join(self.models_dir, MODEL_ONNX)

        # Load the trained scikit-learn model
        model = joblib.load(model_path)

        # Convert the scikit-learn model to ONNX format
        # You should specify the data types and shapes of the input features
        num_input_features = 4
        initial_types = [("input", FloatTensorType([None, num_input_features]))]
        onnx_model = convert_sklearn(model, initial_types=initial_types, target_opset=12)

        # Save the ONNX model to a file
        onnx.save_model(onnx_model, onnx_path)
