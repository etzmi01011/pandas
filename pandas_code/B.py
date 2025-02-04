#create my dataframe using dictionary
import pandas as pd

BabyDataSet={'names':['Bob', 'Jessica', 'Mary',' John', 'Mel',' Jim'], 'births':[968, 155, 77, 578, 973, 968]}
print(BabyDataSet)

df=pd.DataFrame(data=BabyDataSet)
print(df)