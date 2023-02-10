import pytest

import sys
import os

sys.path.append(os.path.abspath('src'))

from xgbrhomut import *


model = XGBPredict(
    im_type="sa_avg", 
    collapse=True
)

prediction = model.make_prediction(
    period=1, 
    damping=0.05, 
    hardening_ratio=0.05, 
    ductility=4, 
    dynamic_ductility=3
)

print(prediction)
