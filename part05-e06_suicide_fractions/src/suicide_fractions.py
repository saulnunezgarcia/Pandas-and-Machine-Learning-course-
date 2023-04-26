#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv('src/who_suicide_statistics.csv')
    df['suicides'] = df['suicides_no']/df['population']
    groups = df.groupby('country')
    return groups['suicides'].mean()

def main():
    suicide_fractions()
    return

if __name__ == "__main__":
    main()
