#!/usr/bin/env python3

import pandas as pd

def top_bands():
    df1 = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep = '\t')
    df2 = pd.read_csv('src/bands.tsv', sep = '\t')
    df2['Band'] = df2['Band'].str.upper()
    return pd.merge(df1,df2,right_on='Band',left_on= 'Artist')

def main():
    top_bands()
    return

if __name__ == "__main__":
    main()
