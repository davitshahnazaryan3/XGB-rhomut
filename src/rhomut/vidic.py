def strength_ratio(mu, T, Tc):
	"""
    Details:
    This implements the R-mu-T relationship proposed by Vidic et al. (1994)

    References:
    Vidic, T., Fajfar, P., and Fischinger, M. [1994] “Consistent inelastic
    design spectra: Strength and displacement,” Earthquake Engineering &
    Structural Dynamics, Vol. 23, No.5, pp. 507–521 DOI: 10.1002/eqe.4290230504.
	
	Parameters
    ----------
    mu:
	T: float
		Period
    Tc: float
        Corner period (called T1 in article)
	Returns
    ----------
	R: float
		Strength ratio
    """

	# Set the empirical coeffienets
	# Choose values for "bilinear, instantaneous stiffness" (4th row) from Table II of Vidic et al (1994)
	c1 = 1.1
	cR = 0.95
	c2 = 0.75
	cT = 0.2

	T0 = c2 * pow(mu, cT) * Tc

	if T < T0:
		R = c1 * pow(mu - 1, cR) * (T / T0) + 1
	else:
		R = c1 * pow(mu - 1, cR) + 1

	return R
