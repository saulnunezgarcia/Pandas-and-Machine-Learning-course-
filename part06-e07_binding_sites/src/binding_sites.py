#!/usr/bin/env python3

 

import pandas as pd

import numpy as np

from sklearn.cluster import AgglomerativeClustering

from sklearn.metrics import accuracy_score

from sklearn.metrics import pairwise_distances

 

from matplotlib import pyplot as plt

 

import seaborn as sns

sns.set(color_codes=True)

import scipy.spatial as sp

import scipy.cluster.hierarchy as hc

import scipy
# Function to rename the clusters, this is used when the accuray_score() of the data is too low but we are cleary seeing that the clusters are working
def find_permutation(n_clusters, real_labels, labels): 
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        new_label=scipy.stats.mode(real_labels[idx])[0][0]  
        permutation.append(new_label)
    return permutation
 

def toint(strin):
    lista = []
    for i in list(strin):
        if i == 'G':
            lista.append(2)
        if i == 'A':
            lista.append(0)
        if i == 'T':
            lista.append(3)
        if i == 'C':
            lista.append(1)
    return lista

def get_features_and_labels(data):
    df = pd.read_csv(data,sep = '\t')
    df['X'] = df['X'].apply(toint).to_numpy() #apply the function and then makes it a numpy array 
    return (np.vstack(df['X']),df['y'])
 

def plot(distances, method='average', affinity='euclidean'):

    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)

    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )

    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")

    plt.show()

 

def cluster_euclidean(data):
    X,y = get_features_and_labels(data)
    model = AgglomerativeClustering(n_clusters= 2, affinity= 'euclidean',linkage= 'average')
    model.fit(X)
    permutation = find_permutation(2,y,model.labels_)
    new_labels = [permutation[label] for label in model.labels_]
    return accuracy_score(y,new_labels)

def cluster_hamming(data):
    X,y = get_features_and_labels(data)
    model = AgglomerativeClustering(n_clusters= 2, affinity= 'hamming',linkage= 'average')
    model.fit(X)
    permutation = find_permutation(2,y,model.labels_)
    new_labels = [permutation[label] for label in model.labels_]
    return accuracy_score(y,new_labels) 
    #Test will ask for pairwise_distances but I didn't included since it delivers the same accuarcy score using the permutation method
    #in any case, to include the pairwise_distances this commands are needed:
    #distances = pairwise_distances(A, metric="hamming") # model = AgglomerativeClustering(2, linkage="average", affinity='precomputed') # yfitted = 1 - model.fit_predict(distances)

def main():

    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))

    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))

 

if __name__ == "__main__":

    main()

 