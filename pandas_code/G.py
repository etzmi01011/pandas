import pandas as pd

df=pd.read_csv("who_suicide_statistics.csv")
print(df.loc[[2,5], 'sex':'suicides_no'])

print(df.loc[0, 'age'])
print(df.loc[0,:])
print(df.loc[0])
