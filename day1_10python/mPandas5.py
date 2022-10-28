# 組合Series物件成DataFrame   mPandas5.py
import pandas as pd
years = range(2019,2022) #[2019,2020,2021]
Blue_peacock = pd.Series([20,18,14],index = years)
Green_peacock = pd.Series([30,25,29],index = years)
White_peacock = pd.Series([5,4,2],index = years)
zoo = pd.concat([Blue_peacock,Green_peacock,White_peacock],axis=1)
print(zoo)
print()
variety = ["Blue_peacock","Green_peacock","White_peacock"]
zoo.columns = variety
print(zoo)

'''
       0   1  2
2019  20  30  5
2020  18  25  4
2021  14  29  2

      Blue_peacock  Green_peacock  White_peacock
2019            20             30              5
2020            18             25              4
2021            14             29              2
'''