#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
#

import cx_Oracle as orcl
import pymongo
import json
import time

if __name__ == "__main__":
	# print(orcl.clientversion())
	# conn = cx_Oracle.connect('uopsett_b_xz/uopsett@192.168.109.2/xz_test')
	# username = "uopsett_b_xz"
	# passwd = "uopsett"
	# host = "192.168.109.2"
	# port = "1521"
	# sid = "xzttest"

	username = "uopsett_b_cz"
	passwd = "uopsett"
	host = "10.0.4.131"
	port = "1521"
	sid = "lct"
	dsn = orcl.makedsn(host, port, sid)
	con = orcl.connect(username, passwd, dsn)

	# mongodb
	client = pymongo.MongoClient()
	db = client.one
	collection = db.tf_f_cardrec
	signal = db.signal

	# tp_dealtime
	#column = ['dealdate', 'dealhour', 'usetage', 'updatetime', 'remark']
	# tf_f_cardrec
	column = ['cardno', 'asn', 'cardtypecode', 'cardsurfacecode', 'manucode', 'chiptypecode', 'appcode', 'appverno', 'deposit', 'cost', 'presupplymoney', 'custrectimecode','selltime', 'sellchannelcode', 'deptno', 'staffno', 'state', 'validenddate', 'usetag','serstarttime', 'serstaketag', 'servicemoney', 'updatestaffno', 'updatetime', 'rsrv1', 'rsrv2','rsrv3', 'remark']
	# print column

	print 'start'
	timestart = time.time()
	print timestart

	cursor = con.cursor()
	sql = "SELECT * FROM tf_f_cardrec"
	cursor.execute(sql);
	#result = cursor.fetchmany(2)
	result = cursor.fetchall()

	timeFetch = time.time()
	print("Total: " + str(cursor.rowcount))
	print 'fetch span:', timeFetch - timestart
	l = []
	i = 0
	count = 0
	for row in result:
		#print(row)
		# print row[1]
		d = dict(zip(column,row))
		l.append(d)
		i += 1
		# 1w条批量插入
		if 10000 == i:			
			collection.insert(l)
			print collection.count()
			signal.insert({'dbsize':collection.count(),"insertNum":10000})
			l = []
			i = 0

		#collection.insert(d)
		# print d

	# print "list", l
	collection.insert(l)
	print len(l)

	cursor.close()
	con.close()

	timeDone = time.time()
	print timeDone
	print 'insert span:', timeDone - timeFetch

	#print(orcl.Date(2015,3,13))
