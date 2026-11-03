from math import sqrt
from scipy.stats import norm

def sampling_distribution(mu: float, sigma: float, n: int, threshold: float) -> dict:
    """
    Returns the sampling mean, sampling standard deviation, and lower-tail probability.
    """
    sampling_std = (sigma/sqrt(n))
    z = (threshold - mu) / sampling_std
    cdf = norm.cdf(z)

    res = {
        "prob_below_threshold": cdf, 
        "sampling_mean": mu,
        "sampling_std": sampling_std,
    }
    return res 