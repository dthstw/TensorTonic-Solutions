import pandas as pd

def unstack_to_wide(data: dict, index_col: str, columns_col: str, values_col: str) -> dict:
    """
    Returns identifier and category column lists, with NaN for missing pairs.
    """
    df = pd.DataFrame(data)
    result = df.set_index([index_col, columns_col])[values_col].unstack().reset_index()
    return result.to_dict(orient="list")
