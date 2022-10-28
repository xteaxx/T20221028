# module copy 是 python內建模組
import copy
before=[1,2,3,4,5,6,7]
after=copy.deepcopy(before)
print(before)
print(after)

after[0]=100
print(before)
print(after)

'''
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[100, 2, 3, 4, 5, 6, 7]
'''