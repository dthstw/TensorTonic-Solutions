import pandas as pd

def iloc_selection(data: dict, row: int, col: int) -> list:
    """
    Returns [element, row_values, col_values], with both value sequences as lists.
    """
    df = pd.DataFrame(data)
    return [df.iloc[row, col], df.iloc[row].to_list(), df.iloc[:, col].to_list()]
