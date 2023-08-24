import pytest
import numpy as np

import sys
import os

sys.path.append(os.path.abspath('src'))

from xgbrhomut.r_mu_t import *


@pytest.mark.rhomut
class RhomutTest:
    @pytest.mark.parametrize("T, R", [
        (0.5, 2.0),
        (1.0, 3.0),
        (1.5, 3.0),
    ])
    def test_ec8(self, T, R):
        assert ec8.strength_ratio(3, T, 1.0) == R

    @pytest.mark.parametrize("case, ahyst, Thyst", [
        ("FD", 0.7, 0.055),
        ("IN", 0.2, 0.030),
        ("SD", 0.0, 0.022),
        ("AA", 0.0, 0.022),
    ])
    def test_guerrini(self, case, Thyst, ahyst):
        if case == "AA":
            with pytest.raises(ValueError):
                guerrini.ductility(4.0, 3.0, 1.0, case, 0.8)

        else:
            expected = abs(3 - (4 + pow(4 - 1, 2.1) /
                           ((1.0 / Thyst + ahyst) * pow(1.0 / 0.8, 2.3))))
            assert guerrini.ductility(4.0, 3.0, 1.0, case, 0.8) == expected

    @pytest.mark.parametrize("ah", [
        (0),
        (2),
        (10),
        (3),
    ])
    def test_krawinkler_nassar(self, ah):
        if ah == 3:
            with pytest.raises(ValueError):
                krawinkler_nassar.strength_ratio(3, 1, ah)
        else:
            assert krawinkler_nassar.strength_ratio(3, 1, ah)

    @pytest.mark.parametrize("site", [
        ("rock"),
        ("soft-soil"),
        ("alluvium"),
        (""),
    ])
    def test_miranda(self, site):
        if site == "":
            with pytest.raises(ValueError):
                miranda.strength_ratio(3, 1, site, 1)
        else:
            assert miranda.strength_ratio(3, 1, site, 1)

    @pytest.mark.parametrize("T, R", [
        (1/50, 1.0),
        (0.1, "compute"),
        (0.3, 3.0),
        (0.8, 4.0),
        (1.2, 5.0),
    ])
    def test_newmark_hall(self, T, R):
        if R == "compute":
            beta = np.log(T / (1. / 33)) / np.log(0.125 / (1. / 33))
            R = pow(2 * 5 - 1, 0.5 * beta)

        assert newmark_hall.strength_ratio(5, T, 0.5, 1.0) == R

    @pytest.mark.parametrize("T, R", [
        (0.5, 3),
        (1.5, 5),
    ])
    def test_vidic(self, T, R):
        assert round(vidic.strength_ratio(5, T, 1.0), 0) == R
