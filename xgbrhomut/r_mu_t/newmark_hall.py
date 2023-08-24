import numpy as np


def strength_ratio(mu: float, period: float,
                   period_cc: float, period_c: float) -> float:
    """This implements the R-mu-T relationship proposed by
    Newmark and Hall (1992)

    References
    ------
    Newmark,  N.  M.,  and  Hall,  W.  J.,  1982,
    Earthquake  Spectra  and  Design,
    Earthquake  Engineering  Research Institute, Berkeley, CA

    Parameters
    ------
    mu : float
        Ductility demand
    period : float
        Period
    period_cc : float
        Corner period (called Tc' in article)
    period_c : float
        Corner period (where the A range transitions to the V range)

    Returns
    ------
    float
        Strength ratio
    """

    # Set the period values based on Newmark and Hall's spectrum
    period_a = 1. / 33
    period_b = 0.125

    beta = np.log(period / period_a) / np.log(period_b / period_a)

    if period < period_a:
        strength_ratio = 1
    elif period <= period_b:
        strength_ratio = pow(2 * mu - 1, 0.5 * beta)
    elif period <= period_cc:
        strength_ratio = pow(2 * mu - 1, 0.5)
    elif period <= period_c:
        strength_ratio = (period / period_c) * mu
    elif period >= period_c:
        strength_ratio = mu

    return strength_ratio
