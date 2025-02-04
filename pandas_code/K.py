import pandas as pd

df=pd.DataFrame(data={'name':['Abby' ,'Bob' ,'Chris']})
df['age']=[20, 15, 28]

df['greater_than_18']=df['age']>18

print(df)

print(df.columns)

df.drop(columns='greater_than_18', inplace=True)
print(df.columns)

print(df)