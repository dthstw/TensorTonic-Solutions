import pandas as pd

def data_types_overview(data: dict) -> dict:
    """
    Returns a dictionary with dtypes, type_counts, and num_columns.
    """
    df = pd.DataFrame(data)
    dtyp = {}
    type_counts = {}
    for col in df.columns:
        dtyp[col] = str(df[col].dtype)
        type_counts[str(df[col].dtype)] = type_counts.get(str(df[col].dtype), 0) + 1
        
    res = {
        "dtypes": dtyp,
        "type_counts": type_counts,
        "num_columns": len(dtyp),
    }
    return res