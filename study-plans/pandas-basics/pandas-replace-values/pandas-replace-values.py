import pandas as pd

def replace_values(data: dict, column: str, old_val: object, new_val: object) -> dict:
    """
    Returns data as a dictionary of updated lists and count as an integer.
    """
    df = pd.DataFrame(data)
    
    count = int(df[column].eq(old_val).sum())
    df[column] = df[column].replace(old_val, new_val)


    res = {
        "data": df.to_dict(orient="list"),
        "count": count,
    }
    
    return res
    
