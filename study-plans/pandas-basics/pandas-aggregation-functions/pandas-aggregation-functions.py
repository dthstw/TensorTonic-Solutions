import pandas as pd

def multi_agg(data: dict, group_col: str, value_col: str, funcs: list) -> dict:
    """
    Returns a dictionary from function names to dictionaries of group aggregates.
    """
    df = pd.DataFrame(data)
    df = df.groupby(group_col)[value_col].agg(funcs)
    return df.to_dict()
