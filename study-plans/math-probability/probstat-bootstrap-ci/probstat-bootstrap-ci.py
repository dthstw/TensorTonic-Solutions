import numpy as np


def bootstrap_ci(data: list, n_bootstraps: int, confidence: float, seed: int) -> list:
    """
    Returns the bootstrap mean and percentile confidence interval.
    """
    samples_means = []
    rand = np.random.RandomState(seed)
    for b in range(n_bootstraps):
        bootstapped = rand.choice(data, replace=True, size=len(data))
        samples_means.append(float(np.mean(bootstapped)))
    alpha = 1 - confidence
    L = 100 * alpha/2
    U = 100 * (1 - alpha/2)
    quantiles = np.percentile(samples_means, q=[L, U])
    mean = round(np.mean(samples_means), 4)
    CI_L = round(float(quantiles[0]), 4)
    CI_U = round(float(quantiles[1]), 4)
    return [mean, CI_L, CI_U]
    
    
