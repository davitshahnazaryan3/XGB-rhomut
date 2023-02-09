import numpy as np


def strength_ratio(mu, T, site, Tg):
	"""
	Details:
	This implements the R-mu-T relationship proposed by Miranda (1993)
	
	References:
	Miranda, E.; Bertero, V. v. (1994).
	Evaluation of Strength Reduction Factors for Earthquake-Resistant Design.
	Earthquake Spectra, 10(2), 357–379. https://doi.org/10.1193/1.1585778

	Parameters
    ----------
	mu: float
		Ductility demand
	T: float
		Period
	site: str
		Site type (options: "rock", "soft-soil" or "alluvium")
	Tg: float
		Predominant period of ground motion (typically around 1s)
	Returns
    ----------
	R: float
		Strength ratio
	"""

	if site.lower() == "rock":
		phi = 1 + 1 / (10 * T - mu * T) - 1 / (2 * T) * np.exp(-3 / 2 * pow(np.log(T) - 3 / 5, 2))
	elif site.lower() == "soft-soil":
		phi = 1 + 1 / (12 * T - mu * T) - 2 / (5 * T) * np.exp(-2 * pow(np.log(T) - 1 / 5, 2))
	elif site.lower() == "alluvium":
		phi = 1 + Tg / (3 * T) - 3 * Tg / (4 * T) * np.exp(-3 * pow(np.log(T / Tg) - 1 / 4, 2))
	else:
		raise ValueError("Wrong site name!")

	R = (mu - 1) / phi + 1

	if R < 1:
		R = 1
		
	return R
