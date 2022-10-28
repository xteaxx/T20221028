# json格式轉乘Python資料 ljson2.py
import json
json_tuple = '(1,2,3,4,5)'
json_array = '[10,20,30,40,50]'
json_object = '{"animal":"Jellyfish","kg":35,"age":100}'

#python_tuple = json.loads(json_tuple)
python_list = json.loads(json_array)
python_dict = json.loads(json_object)

#print(json_tuple,type(json_tuple))
print(json_array,type(json_array))
print(json_object,type(json_object))
print("="*70)
#print(python_tuple, type(python_tuple))
print(python_list, type(python_list))
print(python_dict,type(python_dict))

'''
[10,20,30,40,50] <class 'str'>
{"animal":"Jellyfish","kg":35,"age":100} <class 'str'>
======================================================================
[10, 20, 30, 40, 50] <class 'list'>
{'animal': 'Jellyfish', 'kg': 35, 'age': 100} <class 'dict'>
'''