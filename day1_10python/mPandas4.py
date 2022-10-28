# series 運算   mPandas4.py
import pandas as pd
series_2 = pd.Series([1,3,5,7,9])
series_3 = pd.Series([2,4,6,8,10])
# 四則運算
print(series_2+series_3)
print(series_2-series_3)
print(series_2*series_3)
# 邏輯運算
print(series_2>series_3)
print(series_2<series_3)

'''
0     3     
1     7     
2    11     
3    15     
4    19     
dtype: int64
0   -1      
1   -1      
2   -1      
3   -1      
4   -1      
dtype: int64
0     2
1    12
2    30
3    56
4    90
dtype: int64
0    False
1    False
2    False
3    False
4    False
dtype: bool
0    True
1    True
2    True
3    True
4    True
dtype: bool
'''