import os

import pandas as pd
from sklearn.datasets import load_iris

from ml_pipeline.iris_demo.constants import RAW_DIR


class Download:
    def __init__(self, output_dir: str = RAW_DIR) -> None:
        self.output_dir = output_dir

    def output_path(self) -> str:
        return os.path.join(self.output_dir, "data.csv")

    def __call__(self):
        # Preapre directory if necessary
        os.makedirs(self.output_dir, exist_ok=True)

        # Load the iris dataset
        iris = load_iris()
        data = pd.DataFrame(data=iris.data, columns=iris.feature_names)

        # Add the target variable
        data["target"] = iris.target

        # Save the dataframe to a CSV file
        data.to_csv(self.output_path(), index=False)
