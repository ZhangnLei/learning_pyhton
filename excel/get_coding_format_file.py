import chardet
import xlrd

path = '/Users/zhangdabao/Downloads/alipay_record_20191214_1553_1'

# data = xlrd.open_workbook(path + ".csv")

f = open(r'/Users/zhangdabao/Downloads/alipay_record_20191214_1553_1.csv')
#
data = f.read()

print(chardet.detect(data))

print(chardet.detect(data).get("encoding"))