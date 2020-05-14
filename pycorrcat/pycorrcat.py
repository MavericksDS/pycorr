import warnings
import pandas as pd
import scipy.stats as stats
import numpy as np

def fillna(object):
    if isinstance(object, pd.Series):
        return object.fillna(0)
    else:
        return np.array([value if value is not None else 0 for value in object])

def corr(x, 
         y,
         bias_correction=True,
         Tschuprow=False):
     """
    Calculates correlation statistic for categorical-categorical association.
    The two measures supported are:
    1. Cramer'V ( default )
    2. Tschuprow'T

    Bias correction and formula's taken from : https://www.researchgate.net/publication/270277061_A_bias-correction_for_Cramer's_V_and_Tschuprow's_T
    
    Wikipedia for Cramer's V: https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_V
    Wikipedia for Tschuprow' T: https://en.wikipedia.org/wiki/Tschuprow%27s_T
    Parameters:
    -----------
    x : list / ndarray / Pandas Series
        A sequence of categorical measurements
    y : list / NumPy ndarray / Pandas Series
        A sequence of categorical measurements
    bias_correction : Boolean, default = True
    Tschuprow : Boolean, default = False
               For choosing Tschuprow as measure
    Returns:
    --------
    float in the range of [0,1]
    """
    corr_coeff = np.nan
    try:
        x, y = fillna(x), fillna(y)
        crosstab_matrix = pd.crosstab(x, y)
        n_observations = crosstab_matrix.sum().sum()
        chi2, p, dof, expected = stats.chi2_contingency(crosstab_matrix)
        phi2 = chi2 / n_observations

        # r and c are number of categories of x and y
        r, c = crosstab_matrix.shape
        if bias_correction:
            phi2_corrected = max(0, phi2 - ((r - 1) * (c - 1)) / (n_observations - 1))
            r_corrected  = r - ((r - 1)**2) / (n_observations - 1)
            c_corrected = c - ((c - 1)**2) / (n_observations - 1)
            if Tshcuprow:
                corr_coeff = np.sqrt(phi2_corrected / np.sqrt((r_corrected - 1)*(c_corrected - 1)))
                return corr_coeff
            corr_coeff = np.sqrt(phi2_corrected / min((r_corrected - 1), (c_corrected - 1)))
            return corr_coeff
        if Tschuprow:
            corr_coeff = np.sqrt(phi2 / np.sqrt((r - 1)*(c - 1)))
            return corr_coeff    
        corr_coeff = np.sqrt(phi2 / min((r - 1), (c - 1)))
        return corr_coeff
    except:
        warnings.warn("Error calculating Cramer's V",RuntimeWarning)
        return corr_coeff