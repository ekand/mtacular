# this is a script to collect data from mta
# the intention is to call this from jupyter notebooks

import pandas as pd

# Get data from MTA website according to variables **years** and **months**.
# Generates a wget list in **wget_file** and wgets to **../data**



file_url = 'http://johndoe.com/download.zip'

# file_name = wget.download(file_url)
import urllib

import datetime
import csv
from pathlib import Path


wget_file = '../temp/wget_file.txt'


def get_data(years, months):
    pass


def download_one_file(filename):
    base_url = 'http://web.mta.info/developers/data/nyct/turnstile/'
    url = base_url + filename
    # target_date = datetime.date(2019, 12, 28)

    file_path = raw_data_directory + file_name
    # test_url_getter = urllib.URLopener
    # test_url_getter.retrieve("url", file_path)
    import urllib.request

    print('Beginning file download with urllib2...')

    # url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
    urllib.request.urlretrieve(url, '../../data/raw/cat.jpg')


    return None


# def generate file_list(years, months):
#     pass


if __name__ == "__main__":
    # years = [2018, 2019]
    # months = [3, 4, 5]
    # get_data(years, months)
    #
    # final = datetime.date(2019.12.28)
    # file_delta = datetime.timedelta(days=7)
    # url = 'http://web.mta.info/developers/data/nyct/turnstile/'
    #
    # file_list = []
    print(f"running {str(Path(__file__))}")
    file_name = "turnstile_200104.txt"
    download_one_file(file_name)
    print("tests complete")


