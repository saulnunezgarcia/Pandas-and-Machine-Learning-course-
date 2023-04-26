#!/usr/bin/env python3

 

import numpy as np

from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

 

def fit_line(x,y):
    model = LinearRegression(fit_intercept=True)
    model.fit(np.vstack(x),y)
    return model.coef_[0],model.intercept_

    

def main():

    x = np.array([1, 2, 3])

    y = np.array([1, 2.5, 3]) + 1

    slope, intercept = fit_line(x, y)

    print("Slope:", slope)

    print("Intercept:", intercept)

    plt.scatter(x, y)

    x1 = np.linspace(min(x)-1, max(x)+1, 10)

    plt.plot(x1, x1*slope + intercept, 'red')

    plt.show()

    

if __name__ == "__main__":

    main()