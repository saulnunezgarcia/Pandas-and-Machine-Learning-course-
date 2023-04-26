#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv',sep = '\t')
    return df.loc[0:9,['Title','Artist']]

def main():
    subsetting_by_positions()
    return

if __name__ == "__main__":
    main()
