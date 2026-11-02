from math import exp

def exponential_distribution(lam: float, t: float) -> dict:
    """
    Returns the PDF, CDF, survival probability, mean, and variance.
    """
    pdf = round(lam * exp(-lam * t), 4)
    cdf = round(1 - exp(-lam * t), 4)
    s = round(exp(-lam * t), 4)
    mean = round(1/lam, 4)
    var = round(1/(lam**2), 4)

    res = {
        "pdf": pdf,
        "mean": mean,
        "cdf": cdf, 
        "survival": s,
        "variance": var,
    }
    return res
    
    
