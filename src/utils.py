import pandas as pd

def load_encounters(path: str) -> pd.DataFrame:
    """
    Load patient encounter data from CSV.
    """
    df = pd.read_csv(path)
    # Normalize column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df
