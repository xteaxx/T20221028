# json格式轉成Python資料 ljson2.py
# json格式無法轉成Python的tuple資料
import json
#json_tuple = '(1,2,3,4,5)'
json_array = '[10,20,30,40,50]'

#python_tuple = json.loads(json_tuple)
python_list = json.loads(json_array)

#print(json_tuple,type(json_tuple))
print(json_array,type(json_array))
print("="*70)
#print(python_tuple, type(python_tuple))
print(python_list, type(python_list))