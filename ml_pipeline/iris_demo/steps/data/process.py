import os

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from ml_pipeline.iris_demo.constants import DATA_CSV, RAW_DIR, TEST_DIR, TRAIN_DIR


class Process:
    def __init__(
        self,
        input_dir: str = RAW_DIR,
        output_train_dir: str = TRAIN_DIR,
        output_test_dir: str = TEST_DIR,
        test_ratio: float = 0.2,
        seed: int = 0,
    ) -> None:
        self.input_dir = input_dir
        self.output_train_dir = output_train_dir
        self.output_test_dir = output_test_dir
        self.test_ratio = test_ratio
        self.seed = seed

    def get_description(self) -> dict:
        train_path = os.path.join(self.output_train_dir, DATA_CSV)
        test_path = os.path.join(self.output_test_dir, DATA_CSV)

        return {
            "train_path": train_path,
            "test_path": test_path,
        }

    def __call__(self):
        # Prpare directories
        os.makedirs(self.output_train_dir, exist_ok=True)
        os.makedirs(self.output_test_dir, exist_ok=True)

        # Load the dataset from CSV
        csv_path = os.path.join(self.input_dir, DATA_CSV)
        df = pd.read_csv(csv_path)

        # Assuming all columns except the target are features that need scaling
        # Let's identify all numeric columns first
        # Assuming 'target' is the name of your target column
        numeric_features = df.select_dtypes(include=["float64", "int64"]).columns
        numeric_features = numeric_features.drop("target")

        # Scale the 'sepal length (cm)' feature
        scaler = StandardScaler()
        df[numeric_features] = scaler.fit_transform(df[numeric_features])

        # Splitting the data
        train, test = train_test_split(df, test_size=self.test_ratio, random_state=self.seed)

        # Save the data
        description = self.get_description()
        train.to_csv(description["train_path"], index=False)
        test.to_csv(description["test_path"], index=False)
