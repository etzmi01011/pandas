#output dataframe as csv file
import pandas as pd
names=['Bob', 'Jessica', 'Mary',' John', 'Mel',' Jim']
births=[968, 155, 77, 578, 973, 968]

BabyDataSet=list(zip(names, births))

df=pd.DataFrame(data=BabyDataSet, columns=['names', 'births'])

df.to_csv("birth_data.csv")