import pandas as pd


def csv_to_xlsx_pd():
    path = '/Users/zhangdabao/Downloads/alipay_record_20191214_1553_1'
    csv = pd.read_csv(path+'.csv', encoding='utf-8')
    csv.to_excel(path+'.xlsx', sheet_name='data')


if __name__ == '__main__':
    csv_to_xlsx_pd()
