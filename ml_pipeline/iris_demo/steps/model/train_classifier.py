"""
Train a classifier
- Logistic Regression : ...
- Support Vector Machine (SVM) : ...
- k-Nearest Neighbors (k-NN) : ...
- Decision Trees and Random Forests : ...
- Gradient Boosting Machines (GBM): Models like XGBoost, LightGBM, or CatBoost
"""

import os
import random

import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

from ml_pipeline.iris_demo.constants import ARTIFACTS_DIR, DATA_CSV, MODEL_FILENAME, MODELS_DIR, TRAIN_DIR


class TrainClassifier:
    def __init__(
        self,
        train_dir: str = TRAIN_DIR,
        models_dir: str = MODELS_DIR,
        artifacts_dir: str = ARTIFACTS_DIR,
        seed: int = 0,
    ):
        self.train_dir = train_dir
        self.models_dir = models_dir
        self.artifacts_dir = artifacts_dir
        self.seed = seed

    def set_seed(self):
        random.seed(self.seed)
        np.random.seed(self.seed)

    def load_data(self):
        csv_path = os.path.join(self.train_dir, DATA_CSV)
        data = pd.read_csv(csv_path)
        X_train = data.drop("target", axis=1)
        y_train = data["target"]

        return X_train, y_train

    def __call__(self):
        # Prepare output directories
        os.makedirs(self.models_dir, exist_ok=True)
        os.makedirs(self.artifacts_dir, exist_ok=True)

        # Set seed
        self.set_seed()

        # Get data
        X_train, y_train = self.load_data()

        # Train model
        classifier = LogisticRegression()
        classifier.fit(X_train, y_train)

        # Save model
        model_path = os.path.join(self.models_dir, MODEL_FILENAME)
        joblib.dump(classifier, model_path)
