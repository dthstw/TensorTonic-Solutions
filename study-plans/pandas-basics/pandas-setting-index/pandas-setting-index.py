import pandas as pd

def set_index_column(data: dict, index_col: str) -> dict:
    """
    Returns index_values and columns as lists, plus data as a dictionary of lists.
    """
    df = pd.DataFrame(data).set_index(index_col)
    
    res = {
        "index_values": list(df.index),
        "columns": list(df.columns),
        "data": df.to_dict(orient="list"),
    }
    return res
