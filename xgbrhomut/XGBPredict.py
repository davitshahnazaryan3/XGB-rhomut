import joblib
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import xgboost as xgb


path = Path(__file__).parent.resolve()



class XGBPredict:
    def __init__(self, im_type: str, collapse: bool) -> None:
        """
        Initialize XGB model

        Parameters
        ----------
        im_type: str
            "sa" for R, "sa_avg" for rho2 or rho3
        collapse: bool
            True for collapse scenarios
            False for non-collapse scenarios
            Note: ro_2 is always for non-collapse, while ro_3 is for collapse

        """
        if im_type.lower() == "sa":
            self.parameter = "R"
        elif im_type.lower() == "sa_avg" or im_type.lower() == "saavg":
            if collapse:
                self.parameter = "ro_3"
            else:
                self.parameter = "ro_2"
        else:
            raise ValueError("Wrong im_type, must be 'sa' or 'sa_avg'")

        self.collapse = collapse

    def verify_input(self, period, damping, hardening_ratio, ductility) -> None:
        if not (0.01 <= period <= 3.0):
            warnings.warn("Period is not within recommended limits [0.01, 3.0]")
        
        if not (0.02 <= damping <= 0.2):
            warnings.warn("Period is not within recommended limits [0.02, 0.2]")

        if not (0.02 <= hardening_ratio <= 0.07):
            warnings.warn("Period is not within recommended limits [0.02, 0.07]")

        if not (2.0 <= ductility <= 8.0):
            warnings.warn("Period is not within recommended limits [2.0, 8.0]")
        
    def make_prediction(self, period, damping, hardening_ratio, ductility, dynamic_ductility) -> float:
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
        self.verify_input(period, damping, hardening_ratio, ductility)

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
            "actual_ductility_end": [dynamic_ductility],
        }
        xgb_input = pd.DataFrame.from_dict(xgb_input)
        x = scaler.transform(xgb_input)

        matrix = xgb.DMatrix(x)
        prediction = np.expm1(model.predict(matrix))

        return prediction[0]
