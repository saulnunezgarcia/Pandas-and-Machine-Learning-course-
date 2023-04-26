#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col='Region 2018')
    return df["Akaa":"Äänekoski"]

def swedish_and_foreigners():
    df = municipalities_of_finland()
    df = df[['Population', 'Share of Swedish-speakers of the population, %', 'Share of foreign citizens of the population, %']]
    df = df[df['Share of foreign citizens of the population, %']> 5]
    df = df[df['Share of Swedish-speakers of the population, %']> 5]
    return df

def main():
    swedish_and_foreigners()
    return

if __name__ == "__main__":
    main()
