import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    """Loads dataset from the given filepath."""
    return pd.read_csv(filepath)
