#!/usr/bin/env python3
# encoding: utf-8
import json
import psycopg2
from psycopg2.extras import RealDictCursor
import getopt
import sys

#处理timestamp类型数据
def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj
#定义帮助函数
def help():
    print ("usage: -t user -c user_id,-h,help")
    sys.exit()

#连接数据库
def searchdb(table, columns):
    conn = psycopg2.connect('dbname=surm user=marvin password=marvint')
    cur = conn.cursor(cursor_factory=RealDictCursor)
    db = "SELECT " + columns + " FROM surm." + table
    cur.execute(db)
    data = json.dumps(cur.fetchall(), default=date_handler, ensure_ascii=False, indent=2)
    return data

#获取传参内容，短格式为-t,-c,-h,其中-h不需要传值。
#长格式为--table,--columns,--help，长格式--help不需要传值。
opts,args=getopt.getopt(sys.argv[1:],'t:c:h',["table=","columns=","help"])

#设置默认值变量，当没有传参时就会使用默认值。
table_value="meeting"
columns_value="*"

for opt,value in opts:
    if opt in("-t","--table"):
        table_value=value
       #如果有传参，则重新赋值。
    elif opt in("-c","--columns"):
        columns_value=value
    elif opt in("-h","--help"):
        help()
    else:
        assert False, "unhandled option"

data = searchdb(table_value, columns_value)
print(data)
