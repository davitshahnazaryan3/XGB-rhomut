import pytest

import sys
import os

sys.path.append(os.path.abspath('src'))

from xgbrhomut import *


model = XGBPredict(False, False)
prediction = model.make_prediction(1, 0.05, 0.02, 4, 3)

print(prediction)
