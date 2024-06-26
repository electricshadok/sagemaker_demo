import numpy as np
import onnxruntime

from ml_pipeline.iris_demo.constants import MODEL_ONNX_PATH


class ONNXInference:
    def __init__(self, model_path: str = MODEL_ONNX_PATH):
        self.model_path = model_path

    def __call__(self, input_data: np.ndarray):
        # Load the ONNX model
        sess = onnxruntime.InferenceSession(self.model_path)

        # Prepare the input data
        input_name = sess.get_inputs()[0].name
        inputs = {input_name: input_data.astype(np.float32)}

        # Run inference
        outputs = sess.run(None, inputs)

        return outputs
