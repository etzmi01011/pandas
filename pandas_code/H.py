import pandas as pd
df=pd.read_csv('who_suicide_statistics.csv')

print(df['age'])
print(df.age)
print(df[['age']])
print(df[['age']].shape)
print(df[['age','sex']])
print(df[['age','sex']].shape)