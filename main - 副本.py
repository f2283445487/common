import numpy as np
import pymysql
from dbutils.pooled_db import PooledDB
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
cur = db.cursor(pymysql.cursors.DictCursor)


file = open("sql.txt", 'r')
file_data = file.readlines()
data = []
for row in file_data:
    tmp_list = row.split('/n')
    data.append(tmp_list)


id_list = []
status_list = []
for i in range(len(data)):
    if "WHERE" in data[i][0]:
        id_list.append(data[i+1][0][9:18].replace(' ', '').replace('/', '').replace('*', ''))
        status_list.append(data[i+24][0][10:12].replace(' ', ''))


dd = zip(id_list, status_list)
for i, j in zip(id_list, status_list):
    sql = "UPDATE singa_order.sgo_orders SET order_status = {} where id = {}".format(j, i)
    # print(sql)
    try:
        cur.execute(sql)
        db.commit()
        print("ok")
    except Exception as e:
        print(e)

dd = 80183
# id_list = []
# status_list = []
# for row in data:
#     for i in row:
#         if "@1=" in i:
#             id_list.append(row)
#         elif "@24=" in i:
#             status_list.append(row)
#         else:
#             pass
#
# order_id_list = []
# order_status = []
# for i in range(len(status_list)):
#     if (i % 2) == 0:
#         order_status.append(int(status_list[i][0][10:12].replace(' ', '')))
#
# for i in range(len(id_list)):
#     if (i % 2) == 0:
#         order_id_list.append(int(id_list[i][0][9:17].replace(' ', '').replace('/', '').replace('*', '')))
#
#
# for id, status in zip(order_id_list,order_status):
#     print(id, status)