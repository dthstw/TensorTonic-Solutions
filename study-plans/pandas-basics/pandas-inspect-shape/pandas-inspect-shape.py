import pandas as pd

def inspect_dataframe(data: dict) -> dict:
    """
    Returns rows, cols, columns, dtypes, and total_values in a dictionary.
    """
    df = pd.DataFrame(data)
    types = {}
    for col, typ in df.dtypes.items():
        types[col] = str(typ)
    res = {
        "rows": df.shape[0],
        "cols": df.shape[1],
        'columns': list(df.columns),
        "dtypes": types,
        "total_values": df.shape[0] * df.shape[1],
    }
    
    return res

# What to try: Instead of to_dict, go through the (column name, dtype) pairs that df.dtypes.items() gives you, and convert each dtype with str(...) as you build the dict. Then print type(res["dtypes"]) and type(res["dtypes"]["age"]) on the first example. You should see dict and str.