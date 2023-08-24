def strength_ratio(mu: float, period: float, period_c: float) -> float:
    """This implements the R-mu-T relationship provided in Annex B of
    Eurocode 8 Part 1

    References
    -------
    CEN. [2004] Eurocode 8: Design of Structures for Earthquake Resistance -
    Part 1: General Rules, Seismic Actions and Rules for Buildings
    (EN 1998-1:2004), Brussels, Belgium.

    Parameters
    -------
    mu : float
        Ductility
    period : float
        Period
    period_c : float
        Corner period

    Returns
    -------
    float
        Strength ratio
    """
    if period < period_c:
        strength_ratio = (mu - 1) * (period / period_c) + 1
    else:
        strength_ratio = mu

    return strength_ratio
