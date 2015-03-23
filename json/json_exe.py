#!/usr/bin/env python3
# encoding: utf-8
#from bson import json_util
import json
import psycopg2
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect('dbname=surm user=marvin password=marvint')
cur = conn.cursor(cursor_factory=RealDictCursor)
cur.execute("SELECT * FROM surm.room")

print (json.dumps(cur.fetchall(), ensure_ascii=False))

