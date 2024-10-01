# FILE: src/utils/file_io.py
import pandas as pd

def read_csv(path: str) -> pd.DataFrame:
    """
    Read a CSV file.

    Args:
        path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Data from the CSV file.
    """
    return pd.read_csv(path)

def write_csv(data: pd.DataFrame, path: str) -> None:
    """
    Write a DataFrame to a CSV file.

    Args:
        data (pd.DataFrame): Data to write.
        path (str): Path to the CSV file.
    """
    data.to_csv(path, index=False)