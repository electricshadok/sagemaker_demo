"""
Evaluate a Classifier
evaluation script to check if the model performance meets the specified threshold.
"""

import os

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from ml_pipeline.iris_demo.constants import DATA_CSV, MODEL_FILENAME, MODELS_DIR, TEST_DIR


class EvaluateClassifier:
    def __init__(
        self,
        test_dir: str = TEST_DIR,
        models_dir: str = MODELS_DIR,
    ):
        self.models_dir = models_dir
        self.test_dir = test_dir

    def __call__(self):
        model_path = os.path.join(self.models_dir, MODEL_FILENAME)

        # Load the trained classifier
        classifier = joblib.load(model_path)

        # Load test data
        csv_path = os.path.join(self.test_dir, DATA_CSV)
        test_data = pd.read_csv(csv_path)

        # Separate features and target
        X_test = test_data.drop(columns=["target"])
        y_test = test_data["target"]

        # Make predictions
        y_pred = classifier.predict(X_test)

        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)
        print("Accuracy")
        print(f"{accuracy:.2f}")

        # Generate confusion matrix
        conf_matrix = confusion_matrix(y_test, y_pred)
        print("Confusion Matrix:")
        print(conf_matrix)

        # Generate classification report
        class_report = classification_report(y_test, y_pred)
        print("Classification Report:")
        print(class_report)
