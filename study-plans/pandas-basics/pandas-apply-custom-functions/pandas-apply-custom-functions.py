import pandas as pd

def apply_transform(data: dict, column: str, operation: str) -> dict:
    """
    Returns the original column lists plus the target column with a _transformed suffix.
    """
    df = pd.DataFrame(data)
    if operation == "normalize":
        minn = df[column].min()
        maxx = df[column].max()
        df[f"{column}_transformed"] = ((df[column] - minn) / (maxx - minn)).round(4)
    elif operation == "rank":
        df[f"{column}_transformed"] = df[column].rank().astype("int64")
    elif operation == "cumsum":
        df[f"{column}_transformed"] = df[column].cumsum()
    elif operation == "double":
        df[f"{column}_transformed"] = df[column] * 2
    res = df.to_dict(orient="list")

    return res
