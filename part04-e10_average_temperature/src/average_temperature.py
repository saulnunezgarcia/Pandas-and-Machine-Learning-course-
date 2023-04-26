#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    df = pd.read_csv("src/kumpula-weather-2017.csv",index_col = 'm')
    return df.loc[7,'Air temperature (degC)'].mean()

def main():
    print('Average temperature in July: {}'.format(average_temperature()))
    return

if __name__ == "__main__":
    main()
