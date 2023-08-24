import pytest
import sys
import os

sys.path.append(os.path.abspath('src'))

from xgbrhomut import XGBPredict
from schema import Schema, And, Use, SchemaError


output_schema = Schema({
    'strength_ratio': And(Use(float)),
    'dispersion': And(Use(float))
})


def validate_schema(conf_schema, conf):
    try:
        conf_schema.validate(conf)
        return True
    except SchemaError:
        return False


@pytest.fixture(scope='session')
def collapse_model():
    model = XGBPredict("sa", True)
    return model


@pytest.fixture(scope="session")
def nonCollapse_model():
    model = XGBPredict("sa", False)
    return model


@pytest.mark.predict
class XGBPredictTest:
    @pytest.mark.parametrize("im_type, collapse, expected", [
        ("sa", True, "R"),
        ("SAAVG", False, "ro_2"),
        ("SAAVG", True, "ro_3"),
        ("", True, ValueError),
    ])
    def test_arguments(self, im_type, collapse, expected):
        if im_type != "":
            model = XGBPredict(im_type, collapse)
            assert model.parameter == expected
        else:
            with pytest.raises(expected):
                XGBPredict(im_type, collapse)

    @pytest.mark.parametrize("duct, collapse", [
        (None, True),
        (None, False),
        (4, False),
        (4, True)
    ])
    def test_dynamic_ductility_non_collapse(self, collapse_model, nonCollapse_model, duct, collapse):
        if collapse:
            model = collapse_model
        else:
            model = nonCollapse_model

        if not duct and not collapse:
            with pytest.raises(ValueError):
                model.make_prediction(1, 0.05, 0.05, 3, duct)
        else:
            prediction = model.make_prediction(1, 0.05, 0.05, 3, duct)
            valid = validate_schema(output_schema, prediction)
            assert valid
            