#import pandas, and create my dataframe using list
import pandas as pd

names=['Bob', 'Jessica', 'Mary',' John', 'Mel', 'Jim']
births=[968, 155, 77, 578, 973, 968]

BabyDataSet=list(zip(names, births))

print(BabyDataSet) #output BabyDataSet by list

df=pd.DataFrame(data=BabyDataSet, columns=['names', 'births']) #output BabyDataSet by dataframe
print(df)