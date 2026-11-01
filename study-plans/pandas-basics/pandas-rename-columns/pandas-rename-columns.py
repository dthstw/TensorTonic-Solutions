import pandas as pd

def rename_columns(data: dict, rename_map: dict) -> dict:
    """
    Returns a dictionary mapping renamed column names to their value lists.
    """
    df = pd.DataFrame(data)
    renamed = df.rename(rename_map, axis=1)
    return renamed.to_dict(orient="list")
    
