def ductility(R, *data):
	"""
	Details:
	This implements the R-mu-T relationship proposed by Guerrini et al 2017

	References:
	Guerrini, G., Graziotti, F., Penna, A.;
	Magenes, G. (2017). Improved evaluation of inelastic displacement
	demands for short-period masonry structures. Earthquake Engineering
	&#38; Structural Dynamics, 46(9), 1411–1430.
	https://doi.org/10.1002/eqe.2862
	
	Parameters
    ----------
	R: float
		Strength ratio
	T: float
		Period
	case: str
		See Table II in article, (options: FD, IN, SD)
	Tc: float
		Corner period
	Returns
    ----------
	mu: float
		Ductility demand
	"""
	try:
		mu, T, case, Tc = data
	except ValueError:
		raise ValueError("Wrong input arguments")

	if case.lower() == "fd":
		ahyst = 0.7
		Thyst = 0.055
	elif case.lower() == "in":
		ahyst = 0.2
		Thyst = 0.030
	elif case.lower() == "sd":
		ahyst = 0.0
		Thyst = 0.022
	else:
		raise ValueError

	b = 2.3
	c = 2.1

	return abs(mu - (R + pow(R - 1, c) / ((T / Thyst + ahyst) * pow(T / Tc, b))))

