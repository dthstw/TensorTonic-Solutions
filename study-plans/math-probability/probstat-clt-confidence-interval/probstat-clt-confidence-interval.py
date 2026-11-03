import numpy as np
from scipy.stats import norm

def clt_confidence_interval(data: list, confidence: float) -> list:
    """
    Returns the sample mean, standard error, and confidence-interval endpoints.
    """
    arr = np.asarray(data)
    sample_var = float(np.var(arr, ddof=1))
    sample_mean = np.mean(arr)
    std_error = float(sample_var**(0.5)/(len(arr)**(0.5)))
    z = norm.ppf((1 + confidence) / 2)
    conf_interval_up = float(sample_mean + z * std_error)
    conf_interval_down = float(sample_mean - z * std_error)
    return [sample_mean, std_error, conf_interval_down, conf_interval_up]
    
