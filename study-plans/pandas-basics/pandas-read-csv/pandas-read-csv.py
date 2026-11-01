import pandas as pd

def create_dataframe(data: dict) -> dict:
    """
    Returns a dictionary with data, shape [rows, columns], and ordered column names.
    """
    df = pd.DataFrame(data)
    res = {
        "data": df.to_dict(orient="list"),
        "shape": list(df.shape),
        "columns": list(df.columns),
    }
    
    return res
