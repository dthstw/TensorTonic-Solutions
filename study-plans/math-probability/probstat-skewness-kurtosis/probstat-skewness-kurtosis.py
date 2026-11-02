import numpy as np

def skewness_kurtosis(data: list) -> dict:
    """
    Returns adjusted statistics and their interpretations in a dictionary.
    """
    arr = np.asarray(data, dtype=np.float64)
    sample_std = np.std(arr, ddof=1)
    mean = np.mean(arr)
    z = (arr - mean) / sample_std
    z3 = np.power(z, 3)
    z4 = np.power(z, 4)
    n = len(arr)
    skewness = np.round((n/((n-1)*(n-2)))*np.sum(z3), 4)
    kurtosis = np.round(((n*(n+1))/((n-1)*(n-2)*(n-3)))*np.sum(z4) - (3*(n - 1)**2)/((n-2)*(n-3)), 4) 
    if skewness > 0.5: 
        skew = "right-skewed"
    elif skewness < -0.5:
        skew = "left-skewed"
    else:
        skew = "approximately symmetric"

    if kurtosis > 1:
        kurt = "leptokurtic"
    elif kurtosis < -1:
        kurt = "platykurtic"
    else:
        kurt = "mesokurtic"

    res = {
        "skewness": float(skewness),
        "kurtosis": float(kurtosis),
        "skew_interpretation": skew,
        "kurtosis_interpretation": kurt,
    }
    return res
    
    
    