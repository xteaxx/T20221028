import csv
fn = 'D:\\03爬蟲之旅 30天-水母君\\day1_10python\\Book2.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    print(type(csvReader)) # <class '_csv.reader'>
    data = list(csvReader)
    print(type(data)) # <class 'list'>
for row in data:   #list資料結構data,其元素也是list資料結構,而其元素為字串
    print(row)

for row in data:
    print(row[1])