import warnings
from typing import List

import matplotlib as matplotlib
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns


def fillna(object):
    if isinstance(object, pd.Series):
        return object.fillna(0)
    else:
        return np.array([value if value is not None else 0 for value in object])


def corr(x, y, bias_correction=True, Tschuprow=False):
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

        yates_correct = True
        if bias_correction:
            if crosstab_matrix.shape == (2, 2):
                yates_correct = False

        chi2, _, _, _ = stats.chi2_contingency(
            crosstab_matrix, correction=yates_correct
        )
        phi2 = chi2 / n_observations

        # r and c are number of categories of x and y
        r, c = crosstab_matrix.shape
        if bias_correction:
            phi2_corrected = max(0, phi2 - ((r - 1) * (c - 1)) / (n_observations - 1))
            r_corrected = r - ((r - 1) ** 2) / (n_observations - 1)
            c_corrected = c - ((c - 1) ** 2) / (n_observations - 1)
            if Tschuprow:
                corr_coeff = np.sqrt(
                    phi2_corrected / np.sqrt((r_corrected - 1) * (c_corrected - 1))
                )
                return corr_coeff
            corr_coeff = np.sqrt(
                phi2_corrected / min((r_corrected - 1), (c_corrected - 1))
            )
            return corr_coeff
        if Tschuprow:
            corr_coeff = np.sqrt(phi2 / np.sqrt((r - 1) * (c - 1)))
            return corr_coeff
        corr_coeff = np.sqrt(phi2 / min((r - 1), (c - 1)))
        return corr_coeff
    except Exception:
        warnings.warn("Error calculating Cramer's V", RuntimeWarning)
        return corr_coeff


def corr_matrix(
    data: pd.DataFrame,
    columns: List,
    bias_correction: bool = True,
    Tschuprow: bool = False,
) -> pd.DataFrame:
    """
    Calculates correlation for all the columns provided and returns pandas like correlation matrix.
    The two measures supported are:
    1. Cramer'V ( default )
    2. Tschuprow'T

    Parameters:
    -----------
    data : pandas DataFrame
        A pandas DataFrame containing the categorical columns
    columns : list
        A list of categorical columns
    bias_correction : Boolean, default = True
    Tschuprow : Boolean, default = False
               For choosing Tschuprow as measure
    Returns:
    --------
    pandas dataframe object similar to pandas.DataFrame.corr()
    """
    # checking length of columns
    if (
        not columns.__len__() > 0
        or set(data.columns.values).intersection(columns).__len__() > 0
    ):
        ValueError("Check the columns list provided")

    target_data = data.filter(columns)
    cols = target_data.columns.values
    shape = target_data.columns.__len__()

    matrix = np.zeros((shape, shape))
    for x, i in enumerate(cols):
        temp = np.zeros((0, shape))
        for j in cols:
            temp = np.append(
                temp,
                corr(
                    target_data[i],
                    target_data[j],
                    bias_correction=bias_correction,
                    Tschuprow=Tschuprow,
                ),
            )
        matrix[x] = temp

    corr_matrix = pd.DataFrame(data=matrix, index=cols, columns=cols)
    return corr_matrix


def plot_corr(
    data: pd.DataFrame,
    columns: List,
    diagonal: str = False,
    bias_correction: bool = True,
    Tschuprow: bool = False,
) -> matplotlib.axes.Axes:
    """
    Plots correlation matrix for all the columns provided and returns Matplotlib axes.
    The two measures supported are:
    1. Cramer'V ( default )
    2. Tschuprow'T

    Parameters:
    -----------
    data : pandas DataFrame
        A pandas DataFrame containing the categorical columns
    columns : list
        A list of categorical columns
    diagonal :  string
        When true gives a masked version of heatmap
    bias_correction : Boolean, default = True
    Tschuprow : Boolean, default = False
               For choosing Tschuprow as measure
    Returns:
    --------
    ax : matplotlib Axes
    Axes object with the heatmap.
    """
    corr = corr_matrix(
        data, columns, bias_correction=bias_correction, Tschuprow=Tschuprow
    )
    if diagonal:
        mask = np.triu(corr)
        return sns.heatmap(corr, annot=True, mask=mask)
    return sns.heatmap(corr, annot=True)
