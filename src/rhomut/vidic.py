def Vidic_et_al_1994(mu, T, Tc):
	"""
    Details:
    This implements the R-mu-T relationship proposed by Vidic et al. (1994)
    Information:
    Author: Gerard J. O'Reilly
    First Version: April 2020
    Notes:
    References:
    Vidic, T., Fajfar, P., and Fischinger, M. [1994] “Consistent inelastic
    design spectra: Strength and displacement,” Earthquake Engineering &
    Structural Dynamics, Vol. 23, No.5, pp. 507–521 DOI: 10.1002/eqe.4290230504.
    Inputs:
    mu:
    T: period
    Tc: corner period (called T1 in article)
    Returns:
    R: strength ratio
    """

	# Set the empirical coeffienets
	# Choose values for "bilinear, instantaneous stiffness" (4th row) from Table II of Vidic et al (1994)
	c1 = 1.1
	cR = 0.95
	c2 = 0.75
	cT = 0.2

	# Compute the parameters
	T0 = c2 * pow(mu, cT) * Tc

	if T < T0:
		R = c1 * pow(mu - 1, cR) * (T / T0) + 1
	else:
		R = c1 * pow(mu - 1, cR) + 1

	# Return the outputs
	return R
