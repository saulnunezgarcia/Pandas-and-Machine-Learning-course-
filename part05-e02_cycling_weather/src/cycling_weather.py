#!/usr/bin/env python3

import pandas as pd
import numpy as np

days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))

months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1, 13)))

 
def split_date(df):

    d = df["Päivämäärä"].str.split(expand=True)

    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

 

    hourmin = d["Hour"].str.split(":", expand=True)

    d["Hour"] = hourmin.iloc[:, 0]

 

    d["Weekday"] = d["Weekday"].map(days)

    d["Month"] = d["Month"].map(months)

    

    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})

    return d

def split_dates_continues():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep = ';')
    df = df.dropna(axis = 0, how = 'all')
    df = df.dropna(axis = 1, how = 'all')
    df2 = split_date(df)
    return pd.concat([df2,df.drop('Päivämäärä',axis=1)],axis = 1)

def cycling_weather():
    df = split_dates_continues()
    df2 = pd.read_csv('src/kumpula-weather-2017.csv')
    return pd.merge(df2,df,right_on= ['Year','Month','Day'],left_on= ['Year','m','d']).drop(['m','d','Time','Time zone'],axis = 1)

def main():
    cycling_weather()
    return

if __name__ == "__main__":
    main()
