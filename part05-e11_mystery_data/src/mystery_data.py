#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def mystery_data():
    df = pd.read_csv('src/mystery_data.tsv',sep = '\t')
    model = LinearRegression(fit_intercept = False)
    X1 = df['X1']
    X2 = df['X2']
    X3 = df['X3']
    X4 = df['X4']
    X5 = df['X5']
    x = np.vstack([X1,X2,X3,X4,X5])
    y = np.stack(df['Y'])
    model.fit(x.T,y)
    return model.coef_

def main():
    for i in range(5):
        print('Coefficient of X{} is {}'.format(i+1,mystery_data()[i]))
    # print the coefficients here
    
if __name__ == "__main__":
    main()
