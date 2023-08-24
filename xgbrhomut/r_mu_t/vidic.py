def strength_ratio(mu: float, period: float, period_c: float) -> float:
    """This implements the R-mu-T relationship proposed by Vidic et al. (1994)

    References:
    Vidic, T., Fajfar, P., and Fischinger, M. [1994] “Consistent inelastic
    design spectra: Strength and displacement,” Earthquake Engineering &
    Structural Dynamics, Vol. 23, No.5,
    pp.507-521 DOI: 10.1002/eqe.4290230504.

    Parameters
    ------
    mu : float
        Ductility demand
    period : float
            Period
    period_c : float
        Corner period (called T1 in article)

    Returns
    ------
    float
        Strength ratio
    """

    # Set the empirical coeffienets
    # Choose values for "bilinear, instantaneous stiffness" (4th row)
    # from Table II of Vidic et al (1994)
    c1 = 1.1
    cr = 0.95
    c2 = 0.75
    ct = 0.2

    period_0 = c2 * pow(mu, ct) * period_c

    if period < period_0:
        strength_ratio = c1 * pow(mu - 1, cr) * (period / period_0) + 1
    else:
        strength_ratio = c1 * pow(mu - 1, cr) + 1

    return strength_ratio
