#!/usr/bin/env python3

import pandas as pd


def growing_municipalities(df):
    k = len(df['Population change from the previous year, %'])
    s = sum(df['Population change from the previous year, %']>0)
    return s/k


def main():
    data_frame = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    data = data_frame[1:312]
    percentage = growing_municipalities(data) * 100
    print(percentage)
    print(f"Proportion of growing municipalities: {percentage:.1f}%")
    return

if __name__ == "__main__":
    main()
