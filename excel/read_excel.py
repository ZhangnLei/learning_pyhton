# coding=utf-8

import pandas as pd
import xlrd
import xlwt

'''需要先将文件保存为utf-8格式'''

path = '/Users/zhangdabao/Downloads/alipay_record_20191214_1553_1'
a = [4, 7, 8, 9, 10, 11]


def csv_to_xlsx_pd():
    '''文件转换'''
    csv = pd.read_csv(path+'.csv', encoding='utf-8')
    csv.to_excel(path+'.xlsx', sheet_name='data')


def read_file():
    '''读文件'''
    data = xlrd.open_workbook(path+".xlsx")
    data.sheet_names()
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols

    new_data = []
    new_data.append(get_index_data(table.row_values(4)))
    for i in range(nrows):
        if type(table.row_values(i)[11]) == float:
            new_data.append(get_index_data(table.row_values(i)))
    return new_data


def get_index_data(data):
    '''获取指定下标位置的数据'''
    res = []
    for i in a:
        res.append(data[i])
    return res


def save_file(date):
    '''写入文件 保存文件'''
    print("save...")
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('mysheet', cell_overwrite_ok=True)

    # 添加标题
    date[0].pop()
    date[0].append("人数")
    date[0].append("人均金额")

    # 计算平均值
    for i, row in enumerate(date):
        if i > 0:
            date[i].append(float(date[i][4])/int(date[i][5]))

    # 接着就是给指定的单元格写入数据了
    for i, row in enumerate(date):
        for j, col in enumerate(row):
            sheet.write(i, j, col)
    # 保存文件
    book.save(path+"_final.xls")
    print("save success ")


def delete_file():
    '''删除无用文件'''
    pass


csv_to_xlsx_pd()
new_date = read_file()
save_file(new_date)