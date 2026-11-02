from scipy.stats import norm

def normal_distribution(mu: float, sigma: float, x: float) -> dict:
    """
    Returns the z-score, CDF, PDF, and one-standard-deviation probability.
    """
    z = round((x - mu) / sigma, 4)
    pdf = round(norm.pdf(x, mu, sigma), 4)
    cdf = round(norm.cdf(x, mu, sigma), 4)
    cdf1 = round(norm.cdf(mu + sigma, mu, sigma), 4)
    cdf2 = round(norm.cdf(mu - sigma, mu, sigma), 4)
    
    res = {
        "cdf": cdf,
        "pdf": pdf, 
        "prob_within_1_std": cdf1 - cdf2,
        "z_score": z,
    }
    return res
    
