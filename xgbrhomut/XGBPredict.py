import joblib
from pathlib import Path

import numpy as np
import pandas as pd
import xgboost as xgb


path = Path(__file__).parent.resolve()


class XGBPredict:
    def __init__(self, static: bool, collapse: bool) -> None:
        """
        Initialize XGB model

        Parameters
        ----------
        static: bool
            True for static (R) and False for dynamic (rho2 or rho3)
        collapse: bool
            True for collapse scenarios
            False for non-collapse scenarios
            Note: ro_2 is always for non-collapse, while ro_3 is for collapse

        """
        if static:
            self.parameter = "R"
        else:
            if collapse:
                self.parameter = "ro_3"
            else:
                self.parameter = "ro_2"

        self.collapse = collapse

    def make_prediction(self, period, damping, hardening_ratio, ductility, dynamic_ductiliy) -> float:
        """
        Make predictions using the XGB model

        Parameters
        ----------
        period: float
            Period
        damping: float
            Damping ratio
        hardening_ratio: float
            Hardening ratio
        ductility: float
            Hardening ductility of system
        dynamic_ductility: float
            Ductility where the strength ratio is being predicted

        Returns
        ----------
        prediction: float
            Strength ratio (R, ro_2 or ro_3)

        """
        if self.collapse:
            method = "_collapse"
        else:
            method = ""

        # Read the XGB model
        model = joblib.load(path.parents[0] / f"models/{self.parameter}_xgb{method}.sav")

        # Get the scaler
        scaler = joblib.load(path.parents[0] / f"models/{self.parameter}_xgb{method}_scaler.sav")

        # Construct the input parameters
        xgb_input = {
            "period": [period],
            "damping": [damping],
            "hardening_ratio": [hardening_ratio],
            "ductility": [ductility],
            "actual_ductility_end": [dynamic_ductiliy],
        }
        xgb_input = pd.DataFrame.from_dict(xgb_input)
        x = scaler.transform(xgb_input)

        matrix = xgb.DMatrix(x)
        prediction = np.expm1(model.predict(matrix))

        return prediction[0]
