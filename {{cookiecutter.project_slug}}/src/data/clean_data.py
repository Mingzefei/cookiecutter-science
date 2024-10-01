# FILE: src/data/clean_data.py
import pandas as pd

def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    A sample function to clean data.

    Args:
        data (pd.DataFrame): Raw data.

    Returns:
        pd.DataFrame: Cleaned data.
    """
    # 这里只是一个示例，实际的清洗过程将根据你的数据进行
    cleaned_data = data.dropna()
    return cleaned_data