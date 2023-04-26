#!/usr/bin/env python3

import pandas as pd

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

def split_date_continues():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep = ';')
    df = df.dropna(axis = 0, how = 'all')
    df = df.dropna(axis = 1, how = 'all')
    df2 = split_date(df)
    return pd.concat([df2,df.drop('Päivämäärä',axis=1)],axis = 1)

def bicycle_timeseries():
    df = split_date_continues()
    df['Date'] = pd.to_datetime(df[['Year','Month','Day','Hour']])
    df = df.drop(['Day','Month','Year','Weekday','Hour'],axis = 1)
    return df.set_index('Date')

def main():
    bicycle_timeseries()
    return None

if __name__ == "__main__":
    main()
