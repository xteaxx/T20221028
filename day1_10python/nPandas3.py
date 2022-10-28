# 統計函數   nPandas3.py
import pandas as pd
data = {"Blue_peacock":[30,27,22],"Green_peacock":[30,26,24],"White_peacock":[10,15,20]}
location = [1,2,3]
zoo = pd.DataFrame(data,index = location)
print(zoo)
print()
print("總和: ",zoo["Green_peacock"].sum())
print("最多: ",zoo["Green_peacock"].max())
print("最少: ",zoo["Green_peacock"].min())
print("平均: ",zoo["Green_peacock"].mean())
print("中位數: ",zoo["Green_peacock"].median())
print("標準差: ",zoo["Green_peacock"].std())

'''
   Blue_peacock  Green_peacock  White_peacock
1            30             30             10
2            27             26             15
3            22             24             20

總和:  80
最多:  30
最少:  24
平均:  26.666666666666668
中位數:  26.0
標準差:  3.0550504633038935
'''