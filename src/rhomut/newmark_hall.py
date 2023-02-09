import numpy as np


def strength_ratio(mu, T, Tcc, Tc):
	"""
	Details:
	This implements the R-mu-T relationship proposed by Newmark and Hall (1992)
	
	References:
	Newmark,  N.  M.,  and  Hall,  W.  J.,  1982,  Earthquake  Spectra  and  Design,
	Earthquake  Engineering  Research Institute, Berkeley, CA
	
	Parameters
    ----------
	mu: float
		Ductility demand
	Tc: float
		Corner period
	Tcc: float
		Corner period (called Tc' in article)
	Tc: float
		Corner period (where the A range transitions to the V range)
		
	Returns
    ----------
	R: float
		Strength ratio
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

	return R

