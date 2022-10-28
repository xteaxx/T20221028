# 將Python資料轉成json ljson1.py
import json
list_1 = [10,20,30,40,50]
tuple_1 = (1,2,3,4,5)
dict_1 = {'animal' : "Jellyfish", 'kg' : 35, 'age' : 100}

json_list = json.dumps(list_1)
json_tuple = json.dumps(tuple_1)
json_dict = json.dumps(dict_1)

print(json_list,type(json_list))
print(json_tuple,type(json_tuple))
print(json_dict,type(json_dict))
print("="*60)
print(type(list_1))
print(type(tuple_1))
print(type(dict_1))

'''
[10, 20, 30, 40, 50] <class 'str'>
[1, 2, 3, 4, 5] <class 'str'>
{"animal": "Jellyfish", "kg": 35, "age": 100} <class 'str'>
============================================================
<class 'list'>
<class 'tuple'>
<class 'dict'>
'''