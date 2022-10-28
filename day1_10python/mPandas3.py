# 選取資料   mPandas3.py
import pandas as pd
series_1 = pd.Series([0,1,2,3,4,5])
print(series_1)
print()
print(series_1[1:3])
print()
print(series_1[3:])
print()
print(series_1[:3])
print()
print(series_1[-2:])

'''
0    0      
1    1      
2    2      
3    3      
4    4      
5    5      
dtype: int64

1    1      
2    2      
dtype: int64

3    3
4    4
5    5
dtype: int64

0    0
1    1
2    2
dtype: int64

4    4
5    5
dtype: int64
'''