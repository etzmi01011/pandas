import pandas as pd

df=pd.read_csv("who_suicide_statistics.csv")

print(df.head(n=10))
print(df.sample(n=6))

shape=df.shape
print("Shape:", shape)

columns=df.columns
print("Columns:", columns)

index_=df.index
print("Index:", index_)

dtypes=df.dtypes
print("Datatypes:\n", dtypes)

info=df.info()
print("Info:", info)