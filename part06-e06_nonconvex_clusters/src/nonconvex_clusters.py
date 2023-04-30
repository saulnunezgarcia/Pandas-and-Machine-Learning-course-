#!/usr/bin/env python3

 

import pandas as pd

import numpy as np

from sklearn.cluster import DBSCAN

from sklearn.metrics import accuracy_score

 

import scipy
from sklearn.cluster import DBSCAN

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        if -1 in labels[idx]:
            continue 
        new_label=scipy.stats.mode(real_labels[idx])[0][0]  # Choose the most common label among data points in the cluster
        permutation.append(new_label)
    return permutation

def numclusters(labels):   #To get the number of clusters 
    return len(set(labels)) - (1 if -1 in labels else 0) 

def outliners(labels): #To count the number of outliners
    count = 0 
    for i in labels:
        if i == -1:
            count += 1
    return count



 

def nonconvex_clusters():
    score = []
    clusters = []
    outlinernum = []
    df = pd.read_csv('src/data.tsv',sep = '\t')
    eps = np.arange(0.05,0.2,0.05)
    for i in eps:
        model = DBSCAN(eps = i)
        model.fit(df[['X1','X2']])
        permutation = find_permutation(numclusters(model.labels_),df['y'],model.labels_)
        new_labels = [permutation[label] for label in model.labels_]
        if df['y'].nunique() != numclusters(model.labels_):
            score.append(np.nan)
        else:
            score.append(accuracy_score(df['y'],new_labels))
        outlinernum.append(outliners(model.labels_))
        clusters.append(numclusters(model.labels_))
    dfnew = pd.DataFrame({'eps':eps,'Score':score,'Clusters':clusters,'Outliers':outlinernum})
    dfnew = dfnew.astype({'eps': float, 'Score': float, 'Clusters': float, 'Outliers': float})
    return dfnew
 

def main():

    print(nonconvex_clusters())

 

if __name__ == "__main__":

    main()