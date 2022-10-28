# kcsv1.py 
import csv
fn = 'D:\\03爬蟲之旅 30天-水母君\\day1_10python\\Book.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
print(csvReader)
print(type(csvFile))
print(type(csvReader))

'''
<_csv.reader object at 0x0000025F17D31720>
<class '_io.TextIOWrapper'>
<class '_csv.reader'>
'''