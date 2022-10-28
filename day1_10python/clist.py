# 串列(List)元素為整數,浮點數,字串,串列
list_1 = [123,56.97,"Inheritance",[11,22,33]]
print(list_1)
print(list_1[0])
print(list_1[2])
print(list_1[-3])
print(list_1[-1][1])

list_1[2]="Encapsulation"
list_1.append("Polymorphism")
print(list_1)

'''
[123, 56.97, 'Inheritance', [11, 22, 33]]
123
Inheritance
56.97
22
[123, 56.97, 'Encapsulation', [11, 22, 33], 'Polymorphism']
'''