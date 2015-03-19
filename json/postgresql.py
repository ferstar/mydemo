#!/usr/bin/env python3
# encoding: utf-8

import psycopg2

conn = psycopg2.connect(database = 'surm', user = 'marvin', password = 'marvint', host = '127.0.0.1',port='5432')
cur = conn.cursor()

cur.execute('SELECT room_id FROM surm.room')
rows = cur.fetchall()
#print(rows)
for i in rows:
    print(i)

