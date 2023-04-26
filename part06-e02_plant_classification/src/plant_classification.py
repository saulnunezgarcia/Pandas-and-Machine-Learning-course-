#!/usr/bin/env python3

 

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn import naive_bayes

from sklearn import metrics

from sklearn import datasets

from sklearn.naive_bayes import GaussianNB

 

def plant_classification():
    data = datasets.load_iris()
    X = data.data
    y = data.target
    model = GaussianNB()
    X_train,X_test, y_train, y_test = train_test_split(X,y, random_state=0,train_size = 0.8)
    model.fit(X_train,y_train)
    y_fitted = model.predict(X_test)
    return metrics.accuracy_score(y_test,y_fitted)

 

def main():

    print(f"Accuracy is {plant_classification()}")

 

if __name__ == "__main__":

    main()
