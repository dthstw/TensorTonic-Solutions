def basic_probability(p_a: float, p_b: float, p_a_and_b: float) -> list:
    """
    Returns four rounded probability values in the required order.
    """
    union = np.round(p_a + p_b - p_a_and_b, 4)
    p_ac = np.round(1 - p_a, 4)
    p_bc = np.round(1 - p_b, 4)
    p_a_and_bc = np.round(p_a - p_a_and_b, 4)
    return [union, p_ac, p_bc, p_a_and_bc]
    