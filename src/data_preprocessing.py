import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """
    Load dataset from CSV.
    """
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic cleaning steps:
    - Remove duplicates
    - Drop rows fully empty
    """
    df = df.drop_duplicates()
    df = df.dropna(how="all")
    return df


def save_processed(df: pd.DataFrame, save_path: str) -> None:
    """
    Save cleaned dataset to processed folder.
    """
    df.to_csv(save_path, index=False)

