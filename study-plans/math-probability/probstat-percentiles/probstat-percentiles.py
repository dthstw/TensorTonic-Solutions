import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns the requested percentiles as a float64 array.
    """
    arr = np.asarray(x, dtype=np.float64)

    
    prcn = np.percentile(arr, q)
    return prcn
   