#!/usr/bin/env python3

 

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

 


def explained_variance():
    df = pd.read_csv('src/data.tsv',sep = '\t')
    modelPCA = PCA(10)
    modelPCA.fit(df)
    return df.var().values, modelPCA.explained_variance_

 

def main():

    a, v = explained_variance()

    print(sum(a), sum(v))

    print("The variances are:", " ".join([f"{x:.3f}" for x in a]))

    print("The explained variances after PCA are:", " ".join([f"{x:.3f}" for x in v]))

    plt.plot(np.arange(1,11), np.cumsum(v));

    plt.show()

 

if __name__ == "__main__":

    main()