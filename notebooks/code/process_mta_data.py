import pandas as pd
import numpy as np
from pathlib import Path

PROJECT_DIR = str(Path(__file__).resolve().parents[2])


def add_datetime(df):
    """
    adds a datetime column to the mta dataframes
    :param df:
    :return: a dataframe with a new datetime column, generated from

    """
    time = df.DATE + ' ' + df.TIME
    new_col = pd.to_datetime(time)
    df['datetime'] = new_col
    return df


def clean_col_names(df):
    """
    cleans up the column names in the mta dataframe

    :param df: mta dataframe
    :return: mta dataframe with cleaned columns
    """
    before = 'EXITS                                                               '
    df.rename(columns={before: 'EXITS'}, inplace=True)
