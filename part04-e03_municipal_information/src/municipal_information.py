#!/usr/bin/env python3

import pandas as pd

def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t")
    r,c = df.shape
    print('Shape: {},{}'.format(r,c))
    print('Columns:')
    for i in df.columns:
        print(i)
    return


if __name__ == "__main__":
    main()
