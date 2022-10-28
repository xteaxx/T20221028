# 讀出*.json檔  ljson4.py
import json
fn = 'D:\\03爬蟲之旅 30天-水母君\\day1_10python\\test1.json'
with open(fn) as json_obj:
    data1 = json.load(json_obj)
print(data1)
print(type(data1))

fn = 'D:\\03爬蟲之旅 30天-水母君\\day1_10python\\test3.json'
with open(fn,encoding = 'utf-8') as json_obj2: #含中文資料記得加入 encoding = 'utf-8
    data2 = json.load(json_obj2)
print(data2)
print(type(data2))

'''
{'animal': 'Jellyfish', 'kg': 35, 'age': 100}
<class 'dict'>
{'動物': '水母', '公斤': 35, '年紀': 100}
<class 'dict'>
'''