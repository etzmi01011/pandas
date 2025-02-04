import pandas as pd
df=pd.read_csv('who_suicide_statistics.csv')

print(df.sort_values(by='age').head(n=10))
print(df.sort_values('age', ascending=False))
print(df.sort_values(by=['age', 'sex']).head(n=10))