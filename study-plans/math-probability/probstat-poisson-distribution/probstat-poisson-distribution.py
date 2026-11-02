from math import exp, factorial
import numpy as np

def poisson_distribution(lam: float, max_k: int) -> list:
    """
    Returns the PMF list, cumulative probability, and zero-event probability.
    """
    pmf = [lam ** k * exp(-lam)/factorial(k) for k in range(max_k + 1)]
    pmf_rounded = [round(p, 4) for p in pmf]
    p0 = pmf_rounded[0]
    cmf = sum(pmf_rounded)
    return [pmf_rounded, cmf, p0]