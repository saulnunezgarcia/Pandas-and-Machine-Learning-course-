#!/usr/bin/env python3

 

import scipy


from sklearn.datasets import load_iris

from sklearn import cluster

from sklearn import datasets

from sklearn.metrics import accuracy_score

from sklearn.cluster import KMeans

import sklearn


# Function to rename the clusters, this is used when the accuray_score() of the data is too low but we are cleary seeing that the clusters are working
def find_permutation(n_clusters, real_labels, labels): 
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        new_label=scipy.stats.mode(real_labels[idx])[0][0]  
        permutation.append(new_label)
    return permutation

def plant_clustering():
    iris = datasets.load_iris()
    model = KMeans(n_clusters = 3, random_state = 0 )
    model.fit(iris.data,iris.target)
    permutation = find_permutation(3,iris.target,model.labels_)
    new_labels = [permutation[label] for label in model.labels_]
    return accuracy_score(iris.target,new_labels)
 

def main():

    print(plant_clustering())

 

if __name__ == "__main__":

    main()