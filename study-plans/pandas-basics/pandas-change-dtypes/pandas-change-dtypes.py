import pandas as pd

def change_dtype(data: dict, column: str, target_type: str) -> list:
    """
    Returns [dtypes_before, dtypes_after], both dictionaries of column names to dtype strings.
    """
    df = pd.DataFrame(data)
    dtypes_before = df.dtypes
    df[column] = df[column].astype(target_type)
    dtypes_after = df.dtypes
    return [{col: str(dt) for col, dt in dtypes_before.items()}, {col: str(dt) for col, dt in dtypes_after.items()}]
