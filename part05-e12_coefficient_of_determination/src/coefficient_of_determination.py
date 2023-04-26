#!/usr/bin/env python3

 

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import linear_model

def coefficient_of_determination():
    df = pd.read_csv('src/mystery_data.tsv',sep = '\t')
    model = LinearRegression(fit_intercept = True)
    X = df.loc[:, "X1":"X5"]
    y = df.Y
    model.fit(X,y)
    xr2 = model.score(X,y)
    #Part 2 
    model.fit(df.X1.values.reshape(-1,1),y)
    x1r2 = model.score(df.X1.values.reshape(-1,1),y)
    #x2
    model.fit(df.X2.values.reshape(-1,1),y)
    x2r2 = model.score(df.X2.values.reshape(-1,1),y)
    #x3
    model.fit(df.X3.values.reshape(-1,1),y)
    x3r2 = model.score(df.X3.values.reshape(-1,1),y)
    #x4
    model.fit(df.X4.values.reshape(-1,1),y)
    x4r2 = model.score(df.X4.values.reshape(-1,1),y)
    #x5
    model.fit(df.X5.values.reshape(-1,1),y)
    x5r2 = model.score(df.X5.values.reshape(-1,1),y)
    return xr2, x1r2, x2r2, x3r2, x4r2, x5r2

    

def main():
    for i in range(6):
        if i ==0 :
            print('R2-score with feature(s) X: {}'.format(coefficient_of_determination()[0]))
        else:
            print('R2-score with feature(s) X{}: {}'.format(i,coefficient_of_determination()[i]))
    

if __name__ == "__main__":

    main()