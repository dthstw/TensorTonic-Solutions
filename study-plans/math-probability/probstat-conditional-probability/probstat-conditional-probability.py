def conditional_probability(p_a: float, p_b: float, p_a_and_b: float) -> list:
    """
    Returns both rounded conditional probabilities in the required order.
    """
    a_given_b = round(p_a_and_b / p_b, 4)
    b_given_a = round(p_a_and_b / p_a, 4)
    return [a_given_b, b_given_a]