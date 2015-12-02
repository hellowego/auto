#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
#

import cx_Oracle as orcl
import pymongo
import json

if __name__ == "__main__":
	# print(orcl.clientversion())
	# conn = cx_Oracle.connect('uopsett_b_xz/uopsett@192.168.109.2/xz_test')
	username = "uopsett_b_xz"
	passwd = "uopsett"
	host = "192.168.109.2"
	port = "1521"
	sid = "xzttest"
	dsn = orcl.makedsn(host, port, sid)
	con = orcl.connect(username, passwd, dsn)

	# mongodb
	client = pymongo.MongoClient()
	db = client.test
	collection = db.tp_dealtime

	# tp_dealtime
	#column = ['dealdate', 'dealhour', 'usetage', 'updatetime', 'remark']
	# tf_f_cardrec
	# column = ['cardno', 'asn', 'cardtypecode', 'cardsurfacecode', 'manucode', 'chiptypecode', 'appcode', 'appverno', 'deposit', 'cost', 'presupplymoney', 'custrectimecode','selltime', 'sellchannelcode', 'deptno', 'staffno', 'state', 'validenddate', 'usetag','serstarttime', 'serstaketag', 'servicemoney', 'updatestaffno', 'updatetime', 'rsrv1', 'rsrv2','rsrv3', 'remark','materialsfee']


	print column
	cursor = con.cursor()
	sql = "SELECT * FROM tf_f_cardrec"
	cursor.execute(sql);
	result = cursor.fetchone()
	print("Total: " + str(cursor.rowcount))

	for row in result:
		#print(row)
		# print row[1]
		d = dict(zip(column,row))
		collection.insert(d)
		print d

	cursor.close()
	con.close()

	#print(orcl.Date(2015,3,13))
