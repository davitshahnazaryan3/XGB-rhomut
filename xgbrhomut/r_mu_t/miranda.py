import numpy as np


def strength_ratio(mu: float, period: float, site: str,
                   period_g: float) -> float:
    """This implements the R-mu-T relationship proposed by Miranda (1993)

    References:
    Miranda, E.; Bertero, V. v. (1994).
    Evaluation of Strength Reduction Factors for Earthquake-Resistant Design.
    Earthquake Spectra, 10(2), 357-379. https://doi.org/10.1193/1.1585778

    Parameters
    ------
    mu : float
        Ductility demand
    period : float
        Period
    site : str
        Site type (options: "rock", "soft-soil" or "alluvium")
    period_g : float
        Predominant period of ground motion (typically around 1s)

    Returns
    ------
    float
        Strength ratio
    """

    if site.lower() == "rock":
        phi = 1 + 1 / (10 * period - mu * period) - 1 / (2 * period) * \
            np.exp(-3 / 2 * pow(np.log(period) - 3 / 5, 2))
    elif site.lower() == "soft-soil":
        phi = 1 + 1 / (12 * period - mu * period) - 2 / \
            (5 * period) * np.exp(-2 * pow(np.log(period) - 1 / 5, 2))
    elif site.lower() == "alluvium":
        phi = 1 + period_g / (3 * period) - 3 * period_g / (4 * period) * \
            np.exp(-3 * pow(np.log(period / period_g) - 1 / 4, 2))
    else:
        raise ValueError("Wrong site name!")

    strength_ratio = (mu - 1) / phi + 1

    if strength_ratio < 1:
        strength_ratio = 1

    return strength_ratio
