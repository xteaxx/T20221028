# 自行建立索引   mPandas2.py
import pandas as pd
price = [1000,2000,3000,4000,5000]
size = [100,200,300,400,500]
series_3 = pd.Series(price,index=size)
print(series_3)
print()
weight= [100,10,150]
animals = ['Lion','Jellyfish','Monkey']
series_4 = pd.Series(weight,index=animals)
print(series_4)
print()
print(series_4['Lion'])
print(series_4['Jellyfish'])
print(series_4['Monkey'])
print(series_4.values)
print(series_4.index)

'''
100    1000 
200    2000 
300    3000 
400    4000 
500    5000 
dtype: int64

Lion         100
Jellyfish     10
Monkey       150
dtype: int64    

100
10
150
[100  10 150]
Index(['Lion', 'Jellyfish', 'Monkey'], dtype='object')
'''