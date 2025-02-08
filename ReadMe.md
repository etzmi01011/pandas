# $\Large{Pandas\ 自學\ }$

Pandas就像python裡的Excel，能幫助使用者在python中做到合併與切割各個表格資料的動作。Pandas具備強大的資料分析能力，結合其他python程式庫如numpy能幫助我們進入資料科學的領域。
## 大綱
* [DataFrame物件的建立、讀取、與儲存](#DataFrame物件的建立、讀取、與儲存)
    - [使用list建立dataframe](#使用list建立dataframe)
    - [使用dictionary建立dataframe](#使用dictionary建立dataframe)
    - [將資料儲存成csv檔](#將資料儲存成csv檔)
    - [讀取csv檔為dataframe](#讀取csv檔為dataframe)
* [DataFrame物件的常用屬性與方法](#DataFrame物件的常用屬性和方法)
    - [觀察資料](#觀察資料)
    - [欄位資料型態與描述](#欄位資料型態與描述)
* [DataFrame物件的操作](#DataFrame物件的操作)
    - [使用dataframe的索引](#使用dataframe的索引)
    - [挑選特定欄位的的資料](#挑選特定欄位資料)
    - [篩選資料](#篩選資料)
    - [增加與刪除欄位](#增加與刪除欄位)
    - [合併多個dataframe](合併多個dataframe)

## 載入套件

使用windows+R開啟cmd，並輸入pip install pandas即可於電腦安裝pandas套件。在編譯器編寫程式時則須輸入import pandas as pd，代表匯入pandas並以pd於往後程式碼代稱pandas。
```python
import pandas as pd
```

## DataFrame物件的建立、讀取、與儲存

使用pandas建立一個表格資料並不困難，我們只需要提供資料內容以及欄位的名稱即可。最常見的是用列表(list)或是字典(dictionary)提供我們的資料給pandas。
- ### 使用list建立dataframe

手動將資料輸入後，用list將其合併再轉換成dataframe型態。
```python
#import pandas, and create my dataframe using list
import pandas as pd

names=['Bob', 'Jessica', 'Mary',' John', 'Mel', 'Jim']
births=[968, 155, 77, 578, 973, 968]

BabyDataSet=list(zip(names, births))

print(BabyDataSet) #output BabyDataSet by list

df=pd.DataFrame(data=BabyDataSet, columns=['names', 'births']) #output BabyDataSet by dataframe
df
```
- ### 使用dict建立dataframe

除了使用list外，我們也可以使用dictionary的方式儲存。
```python
#create my dataframe using dictionary
import pandas as pd

BabyDataSet={'names':['Bob', 'Jessica', 'Mary',' John', 'Mel',' Jim'], 'births':[968, 155, 77, 578, 973, 968]}
print(BabyDataSet)

df=pd.DataFrame(data=BabyDataSet)
df
```
- ### 將資料儲存成csv檔案

要將資料輸出成csv檔，可以使用to_csv(“檔案路徑”)實現。
```python
df.to_csv("birth_data.csv")
```
- ### 讀取外部csv檔案為dataframe

使用read_csv可以從外部讀取csv檔並轉成dataframe的型態。
```python
df = pd.read_csv("birth_data.csv", index_col = 0)
df
```

---
## DataFrame物件的常用屬性和方法

在輸入或讀取完資料後，pandas也提供許多函式方便我們觀察以及了解資料。
- ### 觀察資料
使用.head()可以查看前幾筆的資料，如.head(n=10)可查看前10筆數據，若括號內未輸入數字則預設為前5筆數據。
```python
#upload our data file
df=pd.read_csv("who_suicide_statistics.csv")
#use .head(n=10) to observe the first 10 data
#if the () was left blank and it will be defualt by 5
df.head() 
```

使用.sample()可以隨機抽樣指定數量的數據，如.sample(n=6)則是隨機抽樣6筆數據。
```python
#use .semple(n=6) to ramdomly ouput 6 data
#as its ramdomly output, the index order will be ramdom
df.sample(n=6)
```
由於是隨機抽樣，所以可以看到輸出的引索值順序是亂的。
- ### 欄位資料型態與描述
.shape可以查看資料筆數與欄位數量，輸出格式為(資料數量, 欄位數量)。
```python
shape=df.shape
print("Shape:", shape)
```
.columns可以查看資料內欄位名稱。
```python
columns=df.columns
print("Columns:", columns)
```
.index會回傳資料內的列引索。
```python
index_=df.index
print("Index:", index_)
```
.dtypes可以顯示各個欄位的資料型態。
```python
dtypes=df.dtypes
print("Datatypes:\n", dtypes)
```
.info()可以知道各欄位的數量、資料型態以及記憶體配置。
```py
info=df.info()
print("Info:", info)
```
---
## DataFrame物件的操作
- ### 使用dataframe的索引
#### .iloc
```py
# 挑選df中第一列第一欄的資料
df.iloc[0, 0]
```
```py
# 挑選df中第一欄的所有資料
df.iloc[:, 0]
```
```py
# 挑選df中第二列的所有資料
df.iloc[1]
```
####  .loc

```py
# 挑選index=0且欄位為age的資料
df.loc[0, 'age']
```
```py
# 挑選index=0的所有欄位資料-1
df.loc[0, :]
```
```py
# 挑選index為0的所有欄位資料，與上面的程式碼結果相同
df.loc[0]
```
```py
# 挑選index為2或5且從sex 到suicide_no 的資料
df.loc[[2, 5], 'sex':'suicides_no']
```
- ### 挑選特定欄位之資料

在Pandas內還有最後一種使用中括號的方式，功能是取得資料中的特定欄位資料。以下我們試著使用看看。
```py
#挑選age欄位的資料且回傳series類型-1
df['age']
```
```py
#挑選age欄位資料且回傳series類型-2
df.age
```
```py
#挑選age欄位資料且回傳dataframe類型
df[['age']]
```
```py
#挑選age和sex兩欄位資料
df[['age', 'sex']]
```
- ### 篩選資料
```py

#設定篩選的條件並以布林值輸出
condition=(df.age=='15-24 years')

print(condition.head())
```
```py
#放入loc篩選，且只呈現前十筆
df.loc[condition].head(n=10)
```
```py
#篩選多種條件
print(df.loc[(df.age=='15-24 years')&(df['sex']=='male')].head(n=10))
```
```py
#使用.isin()篩選多種條件
print(df.loc[df.age.isin(['15-24 years', '5-14 years'])].head(n=10))
```
- ### 增加與刪除欄位

我們可以使用下面的方法在一個dataframe中增加或減少欄位。

初始dataframe初始dataframe
```py
df = pd.DataFrame(data={'name':['Abby', 'Bob', 'Chris']})
df
```
```py
#將age增加至原本只有name的dataframe
df['age']=[20, 15, 28]
df
```
```py
#新增一欄位判斷age是否大於18歲
df['greater_than_18']=df['age']>18
df
```
```py
#刪除欄位
df.drop(columns='greater_than_18', inplace=True)
df
```
- ### 合併多個dataframe
- #### 使用concat合併dataframe
```py
# 產生範例資料，其中df1與df2的欄位名稱皆相同

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']}, index=[0, 1, 2, 3])


df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']}, index=[4, 5, 6, 7])
df1
df2
```
```py
# 沿著列的方向將兩份資料合併，相同名稱的欄位將會被視為同一個欄位
result = pd.concat([df1, df2])
result
```
```py
# 沿著列的方向將兩份資料合併，並且以keys函數新增index索引
result = pd.concat([df1, df2], keys=['dataframe1', 'dataframe2'])
result
```
```py
# 沿著欄的方向將兩份資料合併，相同的index相會被視為同一筆資料
# 在此由於df1與df2的index數值皆不相同，因此合併後的資料會有八筆
result = pd.concat([df1, df2], axis=1)
result
```
#### 使用merge合併dataframe
```py
# 建立兩個datafrmae，後續會依照key1與key2將其合併

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
result = pd.merge(left, right, on=['key1', 'key2'], how='left')
result
```

## 參考資料
[pandas介紹](https://medium.com/seaniap/pandas/)

[pandas模組介紹](https://utrustcorp.com/python-pandas/)

[pandas教學](https://yhtechnote.com/python-pandas/)

[100-pandas-puzzles](https://github.com/ajcr/100-pandas-puzzles/)
