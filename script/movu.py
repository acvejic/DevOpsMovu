#!/usr/bin/python

import requests
import sys
import psycopg2
from subprocess import call

ip = sys.argv[1]

print ip
URL = 'http://freegeoip.net/csv/' + ip
print URL
response = requests.get(URL)

csv_data = response.text
print csv_data 

#db_exists = call(["su - postgres -c","\'psql -lqt | cut -d \| -f 1 | grep -qw geo_test\'"])
db_exists = 0

if not db_exists:
    con = psycopg2.connect(dbname='postgres', user='dev_ops', host='127.0.0.1', password='devopstest')
    cur = con.cursor()
    cur.execute("CREATE DATABASE geo_test;")

#cur.execute("select * from information_schema.tables where table_name=geo_test_data;")
#bool(cur.rowcount)

con = psycopg2.connect(dbname='geo_test', user='dev_ops', host='127.0.0.1', password='devopstest')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS geo_test_data")
cur.copy_from(csv_data, 'geo_test_data', sep=',', null='')
