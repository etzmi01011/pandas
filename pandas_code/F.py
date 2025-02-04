import pandas as pd

df=pd.read_csv("who_suicide_statistics.csv")
print(df.iloc[0,0])
print(df.iloc[:,0])
print(df.iloc[1])