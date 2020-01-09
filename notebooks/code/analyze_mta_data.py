
import numpy as np
import pandas as pd

## data has been processed and cleaned
## by that I mean you've applied the processing chain in process_mta_data.py
## now let's work on this problem


def group_by_days(df):
    """
    """
    return df.groupby(['CA', 'UNIT', 'SCP', 'STATION', 'DATE']).agg({'INS': 'sum', 'OUTS': 'sum'})

def group_by_station(df):
    return df.groupby(['STATION','DATE']).agg({'INS':'sum', 'OUTS':'sum'})


# def get_daily_station_sums(df):
#     """
#     """
#     df['DATE'] = df.index.get_level_values('DATE')


def get_station_freqs(df):
    """
    apply to df after applying group_by_days and group_by_station
    """
    #df['DATE'] = df.index.get_level_values('DATE')
    df['DAY'] = [d.dayofweek for d in df.index.get_level_values('DATE')]
    return df.groupby(['STATION', 'DAY']).agg({'INS':'median', 'OUTS':'median'})
    



def mean_weekday_rankings(df):
    df = df.drop(index=5, level='DAY')
    df = df.drop(index=6, level='DAY')
    return df.groupby(['STATION']).agg({'INS':'mean', 'OUTS':'mean'}).sort_values('INS', ascending=False)
