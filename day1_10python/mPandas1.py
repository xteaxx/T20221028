# pandas 為第三方模組,必須在終端機上(C:\Users\chts\AppData\Local\Programs\Python\Python310\Scripts)
# 執行 pip install pandas
#使用串列建立Serial物件   mPandas1.py
import pandas as pd   
series_1 = pd.Series([1,2,3,4,5])
print(series_1,type(series_1))   # dtype: int64 <class 'pandas.core.series.Series'>
print()
series_1[2] = 33
print(series_1)

#使用字典建立Serial物件
dictionary = {'動物':'水母','重量':10,'年齡':1}
series_2 = pd.Series(dictionary)
print(series_2,type(series_2))

'''
0    1      
1    2      
2    3      
3    4      
4    5      
dtype: int64 <class 'pandas.core.series.Series'>

0     1
1     2
2    33
3     4
4     5
dtype: int64
動物    水母
重量    10
年齡     1
dtype: object <class 'pandas.core.series.Series'>
'''