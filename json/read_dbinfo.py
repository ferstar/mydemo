import json
import getopt
import sys

import psycopg2
from psycopg2.extras import RealDictCursor





# ����timestamp�������
def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


# ���������
def help():
    print("usage: -t user -c user_id,-h,help")
    sys.exit()


# ������ݿ�
def searchdb(table, columns):
    conn = psycopg2.connect('dbname=surm user=marvin password=marvint')
    cur = conn.cursor(cursor_factory=RealDictCursor)
    db = "SELECT " + columns + " FROM surm." + table
    cur.execute(db)
    data = json.dumps(cur.fetchall(), default=date_handler, ensure_ascii=False, indent=2)
    return data

# ��ȡ�������ݣ��̸�ʽΪ-t,-c,-h,����-h����Ҫ��ֵ��
#����ʽΪ--table,--columns,--help������ʽ--help����Ҫ��ֵ��
opts, args = getopt.getopt(sys.argv[1:], 't:c:h', ["table=", "columns=", "help"])

#����Ĭ��ֵ��������û�д���ʱ�ͻ�ʹ��Ĭ��ֵ��
table_value = "meeting"
columns_value = "*"

for opt, value in opts:
    if opt in ("-t", "--table"):
        table_value = value
        #����д��Σ������¸�ֵ��
    elif opt in ("-c", "--columns"):
        columns_value = value
    elif opt in ("-h", "--help"):
        help()
    else:
        assert False, "unhandled option"

data = searchdb(table_value, columns_value)
print(data)
