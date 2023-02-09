def Krawinkler_Nassar_1992(mu, T, ah):
	"""
	Details:
	This implements the R-mu-T relationship proposed by Krawinkler and Nassar (1992)
	Information:
	Author: Gerard J. O'Reilly
	First Version: September 2022
	Notes:
	References:
	Krawinkler,  H.,  and  Nassar,  A.  A.,  1992,  Seismic  design  based
	on  ductility  and  cumulative  damage  demands   and   capacities,
	Nonlinear   Seismic   Analysis   and   Design   of   Reinforced
	Concrete   Buildings, P. Fajfar and H. Krawinkler, Eds.,
	Elsevier Applied Science, New York, 1992.
	Inputs:
	mu:
	T: period
	ah: hardening ratio (options: 0, 2, 10 in %)
	Returns:
	R: strength ratio
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
		raise ValueError

	c = pow(T, a) / (1 + pow(T, a)) + b / T

	R = pow(c * (mu - 1) + 1, 1 / c)

	# Return the outputs
	return R
