import numpy as np


def Newmark_Hall_1992(mu, T, Tcc, Tc):
	"""
	Details:
	This implements the R-mu-T relationship proposed by Newmark and Hall (1992)
	Information:
	Author: Gerard J. O'Reilly
	First Version: September 2022
	Notes:
	References:
	Newmark,  N.  M.,  and  Hall,  W.  J.,  1982,  Earthquake  Spectra  and  Design,
	Earthquake  Engineering  Research Institute, Berkeley, CA
	Inputs:
	mu:
	T: period
	Tcc: corner period (called Tc' in article)
	Tc: corner period (where the A range transitions to the V range)
	Returns:
	R: strength ratio
	"""

	# Set the period values based on Newmark and Hall's spectrum
	Ta = 1. / 33
	Tb = 0.125

	beta = np.log(T / Ta) / np.log(Tb / Ta)

	if T < Ta:
		R = 1
	elif T <= Tb:
		R = pow(2 * mu - 1, 0.5 * beta)
	elif T <= Tcc:
		R = pow(2 * mu - 1, 0.5)
	elif T <= Tc:
		R = (T / Tc) * mu
	elif T >= Tc:
		R = mu
	else:
		raise ValueError

	# Return the outputs
	return R

