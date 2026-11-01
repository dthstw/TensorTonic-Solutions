import pandas as pd

def concat_dataframes(dfs: list) -> list:
    """
    Returns [shape, data], with shape [rows, columns] and data a dictionary of lists.
    """
    df_list = []
    for df in dfs:
        df_list.append(pd.DataFrame(df))
    res = pd.concat(df_list)
    return [list(res.shape), res.to_dict(orient="list")]
    