# 使用元素為字典的串列建立DataFrame   nPandas1.py
import pandas as pd 
data_1 = [{"Blue_peacock":20,"Green_peacock":30,"White_peacock":5},{"Blue_peacock":18,"Green_peacock":25,"White_peacock":4}]
years_1 = ["2019年","2020年"]
zoo_1 = pd.DataFrame(data_1,index = years_1)
print(zoo_1)
print()

# 使用字典建立DataFrame
data_2 = {"Blue_peacock":[20,18],"Green_peacock":[30,25],"White_peacock":[5,4]}
years_2 = ["2019年","2020年"]
zoo_2 = pd.DataFrame(data_2,index = years_2)
print(zoo_2)

'''
       Blue_peacock  Green_peacock  White_peacock 
2019年            20             30              5
2020年            18             25              4

       Blue_peacock  Green_peacock  White_peacock 
2019年            20             30              5
2020年            18             25              4
'''