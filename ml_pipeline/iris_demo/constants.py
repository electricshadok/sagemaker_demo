import os


#  Directories
RAW_DIR = "./data/raw"
TRAIN_DIR = "./data/processed/train"
VALID_DIR = "./data/processed/valid"
TEST_DIR = "./data/processed/test"
MODELS_DIR = "./training/models/"
ARTIFACTS_DIR = "./training/artifacts/"

# Filenames
DATA_CSV = "data.csv"
MODEL_FILENAME = "model.joblib"
MODEL_ONNX = "model.onnx"
MODEL_ONNX_PATH = os.path.join(MODELS_DIR, MODEL_ONNX)
