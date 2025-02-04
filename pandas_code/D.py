#read csv file and turm into dataframe
import pandas as pd
df=pd.read_csv("birth_data.csv", index_col=0)

print(df)

