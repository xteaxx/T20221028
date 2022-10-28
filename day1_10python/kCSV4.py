# kcsv4.py 寫入csv
import csv
print("這是list資料結構")
fn = 'D:\\03爬蟲之旅 30天-水母君\\day1_10python\\Book2.csv'
with open(fn, 'w', newline ="") as csvFile:
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['Jellysish','white','100'])
    csvWriter.writerow(['Lion','yellow','150'])
    csvWriter.writerow(['Bird','red','1'])
print("儲存成功")

'''
這是list資料結構
儲存成功

# book2.csv內容
Jellysish,white,100
Lion,yellow,150
Bird,red,1
'''