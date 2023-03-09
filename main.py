import pymysql as pymysql
from dbutils.pooled_db import PooledDB
import xlwt

"""TABLE_CATALOG as "表类型", TABLE_SCHEMA as "所属库名称",TABLE_NAME as "表名称","""
pool_db = PooledDB(
    creator=pymysql,
    maxconnections=10,
    mincached=1,
    maxcached=5,
    blocking=True,
    maxusage=None,
    ping=0,
    host="47.241.59.177",
    user="singa_fgh",
    password="rRT@swtm7y",
    # database="singa_origin",
    port=9897,
    autocommit=True
)
db = pool_db.connection()
cur = db.cursor()
title = ['字段名称', '字段类型', '字段注释']

"""pymysql.cursors.DictCursor"""
sql = 'select COLUMN_NAME as "字段名称", COLUMN_TYPE as "字段类型", COLUMN_COMMENT as "字段注释" from information_schema.COLUMNS ' \
      'where TABLE_SCHEMA = "{}" and TABLE_NAME = "{}" '


def get_data(database, table_name):
    cur.execute(sql.format(database, table_name))
    data = cur.fetchall()
    return data


def write_excel(database, table_name):
    data = get_data(database, table_name)
    w = xlwt.Workbook(encoding='utf-8')
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = "微软雅黑"
    style.font = font
    ws = w.add_sheet("info", cell_overwrite_ok=True)
    for line in range(len(title)):
        ws.write(0, line, title[line], style)

    for r in range(len(data)):
        row = data[i]  # 第一行数据
        for j in range(len(row)):
            ws.write(r + 1, j, row[j], style)  # 遍历每个字段  写入这一行

    path = 'database/{}/{}.xls'.format(database, table_name)
    w.save(path)


def export(hhh):
    cur.execute("select TABLE_NAME from information_schema.tables where table_schema = '{}'".format(hhh))
    data = cur.fetchall()
    for r in range(len(data)):
        table_name = data[r]
        for j in table_name:
            write_excel('{}'.format(hhh), j)


if __name__ == '__main__':
    # cur.execute("select TABLE_NAME from information_schema.tables where table_schema = 'singa-origin-rc'")
    # data = cur.fetchall()
    # for i in range(len(data)):
    #     table_name = data[i]
    #     for j in table_name:
    #         write_excel('singa-origin-rc', j)
    database_list = ['sg_data', 'singa_collection', 'singa_fenqi', 'singa_global', 'singa_order', 'singa_origin',
                     'singa_pay', 'singa_rc', 'singa-origin-rc']
    for i in database_list:
        export(i)
