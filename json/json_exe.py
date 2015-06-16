import json

import psycopg2
from psycopg2.extras import RealDictCursor


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


conn = psycopg2.connect('dbname=surm user=marvin password=marvint')
cur = conn.cursor(cursor_factory=RealDictCursor)
cur.execute("SELECT * FROM surm.room")
data = json.dumps(cur.fetchall(), default=date_handler, ensure_ascii=False)
print(data)

