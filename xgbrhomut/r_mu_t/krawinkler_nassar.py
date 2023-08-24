def strength_ratio(mu: float, period: float, ah: float):
    """This implements the R-mu-T relationship proposed by
    Krawinkler and Nassar (1992)

    References
    -------
    Krawinkler,  H.,  and  Nassar,  A.  A.,  1992,  Seismic  design  based
    on  ductility  and  cumulative  damage  demands   and   capacities,
    Nonlinear   Seismic   Analysis   and   Design   of   Reinforced
    Concrete   Buildings, P. Fajfar and H. Krawinkler, Eds.,
    Elsevier Applied Science, New York, 1992.

    Parameters
    -------
    mu : float
        Ductility demand
    period : float
        Period
    ah : float
        Hardening ratio (options: 0, 2, 10 in %)

    Returns
    -------
    float
        Strength ratio

    Raises
    ------
    ValueError
        If hardening ratio is not 0, 2, or 10
    """

    if ah == 0:
        a = 1.
        b = 0.42
    elif ah == 2:
        a = 1.
        b = 0.37
    elif ah == 10:
        a = 0.8
        b = 0.29
    else:
        raise ValueError("Wrong hardening ratio")

    c = pow(period, a) / (1 + pow(period, a)) + b / period

    strength_ratio = pow(c * (mu - 1) + 1, 1 / c)

    return strength_ratio
