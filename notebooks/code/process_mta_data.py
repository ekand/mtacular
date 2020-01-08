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
    df['datetime'] = pd.to_datetime(time)
    return df


def clean_col_names(df):
    """
    cleans up the column names in the mta dataframe

    :param df: mta dataframe
    :return: mta dataframe with cleaned columns
    """
    before = 'EXITS                                                               '
    df.rename(columns={before: 'EXITS'}, inplace=True)
    return df

def add_ins_outs_to_df(df):
    """
    determines the difference of each row's ENTRIES count from the previous row's. It won't diff between different turnstiles, but make sure to run this before any sorting

    :param df: dataframe to manipulate (in place)
    """
    mask = df.duplicated(['CA', 'UNIT', 'SCP', 'STATION'])
    df['INS'] = np.where(mask, df['ENTRIES'] - df['ENTRIES'].shift(1), np.nan)
    df['OUTS'] = np.where(mask, df['EXITS'] - df['EXITS'].shift(1), np.nan)