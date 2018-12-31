#!/usr/bin/python

import xmltodict
import requests
import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

ip = sys.argv[1]
db_user = 'ror_app'
db_password = 'testpass'
db_name = 'geo_test'
db_table_name = 'geo_test_data'
db_host = '127.0.0.1'

con = psycopg2.connect(dbname='postgres', user=db_user, host=db_host, password=db_password)
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = con.cursor()
query = "SELECT COUNT(*) = 0 FROM pg_catalog.pg_database WHERE datname = '" + db_name + "'"
#cur.execute("SELECT COUNT(*) = 0 FROM pg_catalog.pg_database WHERE datname = 'geo_test'")
cur.execute(query)


not_exists_row  = cur.fetchone()
not_exists = not_exists_row[0]

if not_exists:
    query = "CREATE DATABASE " + db_name	
    print ("Database " + db_name + " has been created")
else:
    print ("Database "+ db_name + " exists")

cur.execute(query)
con = psycopg2.connect(dbname=db_name, user=db_user, host=db_host, password=db_password)
cur = con.cursor()
query = "CREATE TABLE IF NOT EXISTS " + db_table_name + " (IP cidr,CountryCode text,CountryName text,RegionCode text,RegionName text,City text,ZipCode integer,TimeZone text,Latitude decimal,Longitude decimal,MetroCode integer);"
cur.execute(query)

URL = 'http://freegeoip.net/xml/' + ip
response = requests.get(URL).content
data = xmltodict.parse(response)['Response']


query =  "INSERT INTO geo_test_data (IP, CountryCode, CountryName, RegionCode, RegionName, City, ZipCode, TimeZone, Latitude, Longitude, MetroCode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

data_values = (data['IP'],data['CountryCode'],data['CountryName'],data['RegionCode'],data['RegionName'],data['City'],data['ZipCode'],data['TimeZone'],data['Latitude'],data['Longitude'],data['MetroCode'])

cur.execute(query,data_values)
con.commit()

for key, value in data.iteritems():
	print key, ": ", value


