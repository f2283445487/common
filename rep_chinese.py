import xlrd
import os


def read_excel(path):
    workbook = xlrd.open_workbook(path, formatting_info=True)
    sheet = workbook.sheet_by_name('info')
    for i in range(1, sheet.nrows):
        old_str = sheet.cell_value(rowx=i, colx=0)
        path = sheet.cell_value(rowx=i, colx=1)
        new_str = sheet.cell_value(rowx=i, colx=2)
        rep(path, old_str, new_str)


def rep(path, old_str, new_str):
    file_data = ''
    with open(path, 'r', encoding='utf-8') as f:
        line = f.read().replace(old_str, new_str, 1)
        file_data += line
    with open(path, 'w', encoding='utf-8') as f:
        f.write(file_data)


if __name__ == '__main__':
    path = r'C:\Users\86172\Desktop\demo\singa-fq.xls'
    read_excel(path)
