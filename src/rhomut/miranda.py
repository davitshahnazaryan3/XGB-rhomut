import numpy as np


def Miranda_1993(mu, T, site, Tg):
	"""
	Details:
	This implements the R-mu-T relationship proposed by Miranda (1993)
	Information:
	Author: Gerard J. O'Reilly
	First Version: September 2022
	Notes:
	References:
	<div class="csl-entry">Miranda, E., &#38; Bertero, V. v. (1994).
	Evaluation of Strength Reduction Factors for Earthquake-Resistant Design.
	<i>Earthquake Spectra</i>, <i>10</i>(2), 357–379. https://doi.org/10.1193/1.1585778</div>
	Inputs:
	mu:
	T: period
	site: site type (options: "rock", "soft-soil" or "alluvium")
	Tg: predominant period of ground motion (typically around 1s)
	Returns:
	R: strength ratio
	"""

	if site == "rock":
		phi = 1 + 1 / (10 * T - mu * T) - 1 / (2 * T) * np.exp(-3 / 2 * pow(np.log(T) - 3 / 5, 2))
	elif site == "soft-soil":
		phi = 1 + 1 / (12 * T - mu * T) - 2 / (5 * T) * np.exp(-2 * pow(np.log(T) - 1 / 5, 2))
	elif site == "alluvium":
		phi = 1 + Tg / (3 * T) - 3 * Tg / (4 * T) * np.exp(-3 * pow(np.log(T / Tg) - 1 / 4, 2))
	else:
		raise ValueError

	R = (mu - 1) / phi + 1

	if R < 1:
		R = 1

	# Return the outputs
	return R
