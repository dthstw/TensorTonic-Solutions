import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns mean, median, and mode as Python floats in a dictionary.
    """
    og, cnts = np.unique(x, return_counts=True)

    res = {
        "mean": np.mean(x),
        "median": np.median(x),
        "mode": float(og[np.argmax(cnts)]),
    }
    return res