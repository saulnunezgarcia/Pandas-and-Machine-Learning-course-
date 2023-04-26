#!/usr/bin/env python3

import pandas as pd
import numpy as np



def special_missing_values():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep = '\t').replace(['New','Re'],np.nan)
    df['LW'] = pd.to_numeric(df['LW'])
    return df[df["Pos"] > df['LW']]

def main():
    special_missing_values()
    return

if __name__ == "__main__":
    main()
