import pandas as pd
df=pd.read_csv('who_suicide_statistics.csv')

condition=(df.age=='15-24 years')


print(condition.head())
print(df.loc[condition].head(n=10))
print(df.loc[(df.age=='15-24 years')&(df['sex']=='male')].head(n=10))
print(df.loc[df.age.isin(['15-24 years', '5-14 years'])].head(n=10))