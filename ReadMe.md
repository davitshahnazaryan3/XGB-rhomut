[![DOI](https://zenodo.org/badge/599498240.svg)](https://zenodo.org/badge/latestdoi/599498240)

# XGBoost - $\rho-\mu-T$

Next-generation non-linear and collapse prediction models for short to long period systems via machine learning methods

The machine learning approach: Exterme Gradient Boosting (XGBoost)

Makes predictions for a strength ratio - ductility - period relationships

Key arguments:

* $R$ - strength ratio based on spectral acceleration
* $\rho$ - strength ratio based on average spectral acceleration
* $\mu$ - ductility
* $T$ - period


$$
  R=\frac{Sa(T)}{Sa_y}
$$

$$
  \rho_2=\frac{Sa_{avg,2}(T)}{Sa_y}
$$

$$
  \rho_3=\frac{Sa_{avg,3}(T)}{Sa_y}
$$

where 

* $Sa(T)$ stands for spectral acceleration at fundamental period
* $Sa_y$ stands for spectral acceleration at yield
* $Sa_{avg,2}(T)$ stands for average spectral acceleration computed at periods 
$∈ [0.2T:2T]$
* $Sa_{avg,3}(T)$ stands for average spectral acceleration computed at periods 
$∈ [0.2T:3T]$

***
## Installation

    pip install xgb-rhomut

***
## Example prediction
Dynamic strength ratio prediction of non-collapse scenarios at a dynamic ductility level of 3.0:

    import xgbrhomut
    model = xgbrhomut.XGBPredict(im_type="sa_avg", collapse=False)
    prediction = model.make_prediction(
      period=1, 
      damping=0.05, 
      hardening_ratio=0.02, 
      ductility=4, 
      dynamic_ductility=3.0
    )
    

prediction:

    {
      "median": float,
      "dispersion": float
    }

    
Other methods

    xgbrhomut.r_mu_t.ec8.strength_ratio(mu=3, T=1, Tc=0.5)

***
## Limitations
Limitations in terms of input parameters are:

* $T$ ∈ [0.01, 3.0] seconds
* $\mu$ ∈ [2.0, 8.0]
* $\xi$ ∈ [2.0, 20.0] %
* $a_h$ ∈ [2.0, 7.0] %
* $a_c$ ∈ [-30.0, -100.0] %
* $R$ ∈ [0.5, 10.0]

where

* $T$ stands for period
* $\mu$ stands for ductility
* $\xi$ stands for damping
* $a_h$ stands for hardening ratio
* $a_c$ stands for softening ratio (necessary to compute fracturing ductility, where collapse is assumed)

Predictions made using the non-linear analysis resutls of 7292 unique SDOF systems amounting in total to 26,000,000 observations (collapse + non-collapse). 

***
## References
* Shahnazaryan D., O'Reilly J.G., 2023, Next-generation non-linear and collapse prediction models for short to long period systems via machine learning methods, *Under Review*
