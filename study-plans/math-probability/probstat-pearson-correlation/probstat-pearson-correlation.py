import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the float64 feature-correlation matrix.
    """
    data = np.asarray(X, dtype=np.float64)
    return np.corrcoef(data, rowvar=False)
    
    