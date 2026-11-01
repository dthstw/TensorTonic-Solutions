import pandas as pd

def drop_duplicates(data: dict) -> list:
    """
    Returns [rows_before, rows_after, cleaned_data], with integer counts and a dictionary of lists.
    """
    df = pd.DataFrame(data)
    dubs = df.duplicated
    cleaned_data = df.drop_duplicates()

    return [df.shape[0], cleaned_data.shape[0], cleaned_data.to_dict(orient="list")]
    
