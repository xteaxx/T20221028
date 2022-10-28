# 將dictionary寫入*.json檔  ljson3.py
import json
# 儲存為 {"animal": "Jellyfish", "kg": 35, "age": 100}
Python_dict = {'animal' : "Jellyfish", 'kg' : 35, 'age' : 100}
fn = 'D:\\03爬蟲之旅 30天-水母君\\day1_10python\\test1.json'
with open(fn,'w') as json_obj:
    json.dump(Python_dict,json_obj)
print("test1.json儲存成功")

# 含中文資料 儲存為 {"\u52d5\u7269": "\u6c34\u6bcd", "\u516c\u65a4": 35, "\u5e74\u7d00": 100}
Python_dict = {'動物' : "水母", '公斤' : 35, '年紀' : 100}
fn = 'D:\\03爬蟲之旅 30天-水母君\\day1_10python\\test2.json'
with open(fn,'w') as json_obj:
    json.dump(Python_dict,json_obj)
print("test2.json儲存成功")

# 含中文資料 儲存為 {"動物": "水母", "公斤": 35, "年紀": 100}
Python_dict = {'動物' : "水母", '公斤' : 35, '年紀' : 100}
fn = 'D:\\03爬蟲之旅 30天-水母君\\day1_10python\\test3.json'
with open(fn,'w',encoding = 'utf-8') as json_obj:   # 加 encoding = 'utf-8'
    json.dump(Python_dict,json_obj,ensure_ascii = False) # 加 ensure_ascii = False
print("test3.json儲存成功")

'''
test1.json儲存成功
test2.json儲存成功
test3.json儲存成功

test1.json內容   {"animal": "Jellyfish", "kg": 35, "age": 100}
test2.json內容   {"\u52d5\u7269": "\u6c34\u6bcd", "\u516c\u65a4": 35, "\u5e74\u7d00": 100}
test3.json內容   {"動物": "水母", "公斤": 35, "年紀": 100}
'''