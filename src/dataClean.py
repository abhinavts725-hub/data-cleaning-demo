from pathlib import Path

import numpy as np
import pandas as pd


def clean_dataset(input_path: str, output_path: str) -> pd.DataFrame:
    """
    Clean the raw electrification dataset and save the processed file.

    Args:
        input_path (str): Path to the raw CSV file.
        output_path (str): Path to save the cleaned CSV file.

    Returns:
        pd.DataFrame: Cleaned DataFrame after validation and transformations.
    """
    # Step 1: Load CSV from disk into a DataFrame.
    df = pd.read_csv(input_path)

    # Step 2: Print missing-value counts before any cleaning operations.
    print("Missing values before cleaning:")
    print(df.isna().sum())