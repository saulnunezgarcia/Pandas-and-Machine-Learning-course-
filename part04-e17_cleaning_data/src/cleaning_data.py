#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    df = pd.read_csv('src/presidents.tsv',sep = '\t')
    df = df.replace('-', np.nan)
    df['Seasons'][3] = 2
    df['Start'][0] = 2017
    mask = df.index.isin([2, 3])  # Select rows with index 2 and 3
    df.loc[mask, 'President'] = df.loc[mask, 'President'].str.split(' ').apply(lambda x: ' '.join(x[::-1]))
    df.loc[mask, 'Vice-president'] = df.loc[mask, 'Vice-president'].str.split(' ').apply(lambda x: ' '.join(x[::-1]))
    df['President'] = df['President'].str.title().str.replace(',','')
    df['Vice-president'] = df['Vice-president'].str.title().str.replace(',','')
    df['President'] = df['President'].astype(str)  # Convert column 1 to object (string)
    df['Start'] = df['Start'].astype('int32')  # Convert column 2 to int
    df['Last'] = df['Last'].astype('float64')  # Convert column 3 to float
    df['Seasons'] = df['Seasons'].astype('int32')  # Convert column 4 to int
    df['Vice-president'] = df['Vice-president'].astype(str)  # Convert column 5 to object (string)
    return df

def main():
    cleaning_data()
    return

if __name__ == "__main__":
    main()
