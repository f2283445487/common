import re
import os
import xlwt
import xlrd


def get_notes(old_path):
    """获取多行注释"""
    with open(old_path, 'r', encoding='utf-8') as f:
        code = f.read()
        result = re.findall(r"/\*{1,2}[\s\S]*?\*/", code)
        notes = re.findall(r'[一-龥]+', str(result))
        return notes


def get_note(old_path):
    """获取单行注释"""
    with open(old_path, 'r', encoding='utf-8') as f:
        code = f.read()
        result = re.findall(r'(?=//).*?(?=[一-龥]+).*?(?=\n)', code)
        note = re.findall(r'[一-龥]+', str(result))
        return note


def remove(file_path):
    notes = get_notes(file_path)
    note = get_note(file_path)
    for i in notes:
        rep(file_path, i, '')
    for i in note:
        rep(file_path, i, '')
    if notes or note:
        remove(file_path)


def write_excel(result, file_path):
    title = ['中文信息', '文件路径', '替换']
    w = xlwt.Workbook(encoding='utf-8')
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = "微软雅黑"
    style.font = font
    ws = w.add_sheet("info", cell_overwrite_ok=True)
    for i in range(len(title)):
        ws.write(0, i, title[i], style)

    code_list = []
    for i in range(len(result)):
        row = result[i]
        for j in range(len(row[0])):
            code_list.append([row[0][j], row[1]])

    for i in range(len(code_list)):
        row = code_list[i]
        for j in range(len(row)):
            ws.write(i + 1, j, row[j], style)
    w.save(file_path)


def get_chinese_code(file_path):
    """获取中文注释 多行注释"""
    f = open(file_path, 'r', encoding='utf-8')
    code = f.read()
    # result = re.findall(r'(?=/*).*(?=[\u4e00-\u9fa5]+).*(?=\*/)|(?=//).*(?=[\u4e00-\u9fa5]+).*(?=\n)', str)
    # result = re.findall(r'(\/\*.*[\u4e00-\u9fa5]+.*\*\/)|(\/\/.*?[\u4e00-\u9fa5]+.*?\n)', str)
    result = re.findall(r'[一-龥]+', code)
    return result, file_path


def rep(file_path, old_str, new_str):
    file_data = ''
    with open(file_path, 'r', encoding='utf-8') as f:
        line = f.read().replace(old_str, new_str, 1)
        file_data += line
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(file_data)


def read_excel(trans_excel_path):
    workbook = xlrd.open_workbook(trans_excel_path, formatting_info=True)
    sheet = workbook.sheet_by_name('info')
    for i in range(1, sheet.nrows):
        old_str = sheet.cell_value(rowx=i, colx=0)
        path = sheet.cell_value(rowx=i, colx=1)
        new_str = sheet.cell_value(rowx=i, colx=2)
        rep(path, old_str, new_str)


if __name__ == '__main__':
    file = r'C:\Users\86172\Desktop\demo'
    # file = r'C:\Users\86172\Desktop\demo'
    chinese_code = []
    for root, dirs, files in os.walk(file):
        for file in files:
            path = os.path.join(root, file)
            if file.endswith('.php'):
                remove(path)
    #             if get_chinese_code(path)[0]:
    #                 chinese_code.append(get_chinese_code(path))
    # print(chinese_code)
    # write_excel(chinese_code, r'./singa-fq2.xls')
    # read_excel()
