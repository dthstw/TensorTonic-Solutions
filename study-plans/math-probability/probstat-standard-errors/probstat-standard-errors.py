import numpy as np

def standard_errors(samples: list) -> dict:
    """
    Returns each sample standard error and their mean.
    """
    vars = [float(np.var(sample, ddof=1)) for sample in samples]
    stds = np.sqrt(vars)
    standard_errors = np.round(stds / [(len(sample) ** 0.5) for sample in samples], 4)
    mean_se = sum(standard_errors) / len(samples)
    return {"mean_se":mean_se,"standard_errors": standard_errors}
    
    