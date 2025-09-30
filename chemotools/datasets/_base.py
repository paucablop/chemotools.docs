import os


import pandas as pd
import polars as pl

PACKAGE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


def load_fermentation_train(set_output="pandas"):
    """Load training partition of the fermentation dataset (synthetic offline spectra).

    Parameters
    ----------
    set_output : {"pandas", "polars"}, default="pandas"
        Output container type.

    Returns
    -------
    train_spectra : pandas.DataFrame or polars.DataFrame
        Synthetic spectra used for calibration.
    train_hplc : pandas.DataFrame or polars.DataFrame
        Corresponding reference (HPLC) measurements.

    References
    ----------
    Cabaneros Lopez Pau, Udugama Isuru A., Thomsen Sune Tjalfe, Roslander Christian, Junicke Helena,
    Mauricio Iglesias Miguel, Gernaey Krist V. "Transforming data into information: A parallel hybrid model for
    real-time state estimation in lignocellulose ethanol fermentations."
    """
    if set_output == "pandas":
        train_spectra = pd.read_csv(PACKAGE_DIRECTORY + "/data/train_spectra.csv")
        train_spectra.columns = train_spectra.columns.astype(float)
        train_hplc = pd.read_csv(PACKAGE_DIRECTORY + "/data/train_hplc.csv")
        return train_spectra, train_hplc

    if set_output == "polars":
        train_spectra = pl.read_csv(PACKAGE_DIRECTORY + "/data/train_spectra.csv")
        train_hplc = pl.read_csv(PACKAGE_DIRECTORY + "/data/train_hplc.csv")
        return train_spectra, train_hplc

    else:
        raise ValueError(
            "Invalid value for set_output. Please use 'pandas' or 'polars'."
        )


def load_fermentation_test(set_output="pandas"):
    """Load test partition of the fermentation dataset (online process spectra).

    Parameters
    ----------
    set_output : {"pandas", "polars"}, default="pandas"
        Output container type.

    Returns
    -------
    test_spectra : pandas.DataFrame or polars.DataFrame
        Online spectra captured during fermentation.
    test_hplc : pandas.DataFrame or polars.DataFrame
        Corresponding HPLC reference measurements.

    References
    ----------
    Cabaneros Lopez Pau, Udugama Isuru A., Thomsen Sune Tjalfe, Roslander Christian, Junicke Helena,
    Mauricio Iglesias Miguel, Gernaey Krist V. "Transforming data into information: A parallel hybrid model for
    real-time state estimation in lignocellulose ethanol fermentations."
    """
    if set_output == "pandas":
        fermentation_spectra = pd.read_csv(
            PACKAGE_DIRECTORY + "/data/fermentation_spectra.csv"
        )
        fermentation_spectra.columns = fermentation_spectra.columns.astype(float)
        fermentation_hplc = pd.read_csv(
            PACKAGE_DIRECTORY + "/data/fermentation_hplc.csv"
        )
        return fermentation_spectra, fermentation_hplc

    if set_output == "polars":
        fermentation_spectra = pl.read_csv(
            PACKAGE_DIRECTORY + "/data/fermentation_spectra.csv"
        )
        fermentation_hplc = pl.read_csv(
            PACKAGE_DIRECTORY + "/data/fermentation_hplc.csv"
        )
        return fermentation_spectra, fermentation_hplc

    else:
        raise ValueError(
            "Invalid value for set_output. Please use 'pandas' or 'polars'."
        )


def load_coffee(set_output="pandas"):
    """Load coffee ATR-FTIR dataset (three origins).

    Parameters
    ----------
    set_output : {"pandas", "polars"}, default="pandas"
        Output container type.

    Returns
    -------
    coffee_spectra : pandas.DataFrame or polars.DataFrame
        Spectral measurements.
    coffee_labels : pandas.DataFrame or polars.DataFrame
        Origin labels for each spectrum.
    """
    if set_output == "pandas":
        coffee_spectra = pd.read_csv(PACKAGE_DIRECTORY + "/data/coffee_spectra.csv")
        coffee_labels = pd.read_csv(PACKAGE_DIRECTORY + "/data/coffee_labels.csv")
        return coffee_spectra, coffee_labels

    if set_output == "polars":
        coffee_spectra = pl.read_csv(PACKAGE_DIRECTORY + "/data/coffee_spectra.csv")
        coffee_labels = pl.read_csv(PACKAGE_DIRECTORY + "/data/coffee_labels.csv")
        return coffee_spectra, coffee_labels

    else:
        raise ValueError(
            "Invalid value for set_output. Please use 'pandas' or 'polars'."
        )
