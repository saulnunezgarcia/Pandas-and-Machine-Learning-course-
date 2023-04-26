#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    df1 = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep = '\t')
    groups = df1.groupby('Publisher')
    a = groups['WoC'].sum().sort_values(ascending = False).idxmax()
    return groups.get_group(a)

def main():
    best_record_company()
    return
    

if __name__ == "__main__":
    main()
