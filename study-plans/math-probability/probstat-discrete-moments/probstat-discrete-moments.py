import numpy as np

def discrete_moments(values: list, probabilities: list) -> list:
    """
    Returns the first moment, second moment, variance, and standard deviation.
    """
    val = np.round(np.asarray(values), 4)
    p = np.round(np.asarray(probabilities), 4)
    val2 = np.round(np.power(val, 2), 4)
    exp = np.sum(val * p)
    exp2 = np.sum(val2 * p)
    var = (round(exp2 - np.power(exp, 2), 4))
    return [exp, exp2, var, np.round(np.sqrt(var), 4)]
    
    
