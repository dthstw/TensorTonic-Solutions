import pandas as pd

def merge_dataframes(left: dict, right: dict, on: str, how: str) -> dict:
    """
    Returns a dictionary of merged column lists, with NaN for unmatched cells.
    """
    dfl = pd.DataFrame(left)
    dfr = pd.DataFrame(right)
    new_df = dfl.merge(dfr, on=on, how=how)
    return new_df.to_dict(orient="list")
