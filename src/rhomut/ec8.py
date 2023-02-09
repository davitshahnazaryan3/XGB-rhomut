def strength_ratio(mu, T, Tc):
    """
    Details:
    This implements the R-mu-T relationship provided in Annex B of Eurocode 8 Part 1

    References:
    CEN. [2004] Eurocode 8: Design of Structures for Earthquake Resistance -
    Part 1: General Rules, Seismic Actions and Rules for Buildings
    (EN 1998-1:2004), Brussels, Belgium.

    Parameters
    ----------
    mu: float
        Ductility
    T: float
        Period
    Tc: float
        Corner period
    Returns
    ----------
    R: float
        Strength ratio
    """
    if T < Tc:
        R = (mu - 1) * (T / Tc) + 1
    else:
        R = mu

    return R
