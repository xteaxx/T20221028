before=[1,2,3,4,5,6,7]
after=before
print(before)
print(after)

after[0]=100
print(before)
print(after)

'''
此處有bug, list儲存記憶體的觀念
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[100, 2, 3, 4, 5, 6, 7]
[100, 2, 3, 4, 5, 6, 7]
'''