#!/usr/bin/env python3

import pandas as pd

def powers_of_series(s1,n):
    lista = []
    df = pd.DataFrame(s1,index = s1.index,columns = [1])
    for n in range(n+1):
        if n>1:
            lista.append(s1**n)
    for i,j in enumerate(lista):
        df[i+2] = j
    return df
    
def main():
    s1 = pd.Series([1,2,3,4,5],index = list('abcde'))
    n = 4
    print(powers_of_series(s1,4))
    return
    
if __name__ == "__main__":
    main()
