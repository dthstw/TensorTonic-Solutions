import pandas as pd

def reset_index_demo(data: dict, index_col: str) -> list:
    """
    Returns [columns_before_reset, columns_after_reset], both lists of strings.
    """
    df = pd.DataFrame(data)
    df = df.set_index(index_col)
    return [list(df.columns), list(df.reset_index().columns)]
    
    
