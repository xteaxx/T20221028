# 使用字典建立DataFrame   nPandas2.py
import pandas as pd
data = {"Blue_peacock":[30,27,22],"Green_peacock":[30,26,24],"White_peacock":[30,28,20]}
years = [2019,2020,2021]
zoo = pd.DataFrame(data,index = years)
print(zoo)
print()
# 索引功能-直接索引
print(zoo['Green_peacock'])
print()
print(zoo['Green_peacock'][2020])
print()
# 索引功能-使用屬性
print("at: ", zoo.at[2019,"Green_peacock"]) # 列,行
print()
print("iat: ", zoo.iat[0,1])
print()
print("loc: ",zoo.loc[2020])
print()
print("iloc:",zoo.iloc[0])

'''
          Blue_peacock  Green_peacock  White_peacock
2019            30             30             30
2020            27             26             28
2021            22             24             20

2019    30
2020    26
2021    24
Name: Green_peacock, dtype: int64

26

at:  30

iat:  30

loc:  Blue_peacock     27
Green_peacock    26
White_peacock    28
Name: 2020, dtype: int64

iloc: Blue_peacock     30
Green_peacock    30
White_peacock    30
Name: 2019, dtype: int64
'''
