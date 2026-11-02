def independence_test(p_a: float, p_b: float, p_a_and_b: float) -> dict:
    """
    Returns the rounded product and independence decision in a dictionary.
    """
    product = p_a * p_b
    is_independent = abs(p_a_and_b - product) <= 1e-9
    return {"p_a_times_p_b": round(product, 4), "is_independent": is_independent}