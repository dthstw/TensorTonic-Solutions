import pandas as pd

def handle_missing(data: dict, fill_value: float) -> dict:
    """
    Returns null_counts as a dictionary of integers and cleaned_data as a dictionary of lists.
    """
    df = pd.DataFrame(data)
    res = {
        "null_counts": df.isna().sum(axis=0).to_dict(),
        "cleaned_data": df.fillna(fill_value).to_dict(orient="list"),
    }
    
    return res 
