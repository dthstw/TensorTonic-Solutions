import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns sample variance and standard deviation as Python floats.
    """
    arr = np.asarray(x, dtype=np.float64)
    var = np.var(arr, ddof=1)
    std = np.sqrt(var)
    return {"variance": var, "std_dev": float(std)}