#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
#

'''
select count(1) from th_trade_right where id like '01%';  57485594   1:03
select count(1) from th_trade_right ;   397937882  3:46
select min(dealtime) from th_trade_right;   2014/1/1  15:12
select max(dealtime) from th_trade_right;  2015/2/28 13:00:00  16:09
select max(inlisttime),min(inlisttime) from th_trade_right;  2015/3/1 2:06:35  2014/1/1 4:12:15  16:34


'''

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

	# username = "uopsett_b_cz"
	username = "uopsett_b_sz"
	passwd = "uopsett"
	# host = "10.0.4.131"
	host = "172.16.128.250"
	port = "1521"
	# sid = "lct"
	sid = "szt"
	dsn = orcl.makedsn(host, port, sid)
	con = orcl.connect(username, passwd, dsn)

	# mongodb
	client = pymongo.MongoClient()
	db = client.one
	# collection = db.tf_f_cardrec
	collection = db.th_trade_right
	signal = db.signal
	dbfetch = db.dbfetch
	

	# tp_dealtime
	#column = ['dealdate', 'dealhour', 'usetage', 'updatetime', 'remark']
	# tf_f_cardrec
	# column = ['cardno', 'asn', 'cardtypecode', 'cardsurfacecode', 'manucode', 'chiptypecode', 'appcode', 'appverno', 'deposit', 'cost', 'presupplymoney', 'custrectimecode','selltime', 'sellchannelcode', 'deptno', 'staffno', 'state', 'validenddate', 'usetag','serstarttime', 'serstaketag', 'servicemoney', 'updatestaffno', 'updatetime', 'rsrv1', 'rsrv2','rsrv3', 'remark']
	# print column

	# nj th_trade_right
	column = ['ID','CARDNO','RECTYPE','ICTRADETYPECODE','ASN','CARDTRADENO','SAMNO','PSAMVERNO','POSNO','POSTRADENO','TRADEDATE','TRADETIME','PREMONEY','TRADEMONEY','SMONEY','TRADECOMFEE','BALUNITNO','CALLINGNO','CORPNO','DEPARTNO','CALLINGSTAFFNO','CITYNO','TAC','TACSTATE','MAC','SOURCEID','BATCHNO','DEALTIME','INLISTTIME','INHISTIME','RSRVCHAR']

	print 'start'
	timestart = time.time()
	print timestart


	# '''

	cursor = con.cursor()
	# sql = "SELECT * FROM th_trade_right where id like '010%'"
	sql = "SELECT * FROM th_trade_right "
	cursor.execute(sql);
	result = cursor.fetchmany(1000000)
	# result = cursor.fetchall()

	timeFetch = time.time()
	fetchspan = timeFetch - timestart
	print("Total: " + str(cursor.rowcount))
	print 'fetch span:', fetchspan

	dbfetch.insert({'collectionName': 'th_trade_right','begintime':timestart, 'endtime':timeFetch, 'fetchspan':fetchspan, 'total':cursor.rowcount})
	l = []
	i = 0
	count = 0
	# 没10w条插入mongodb
	for row in result:
		#print(row)
		# print row[1]
		d = dict(zip(column,row))
		l.append(d)
		i += 1
		# 1w条批量插入
		if 10000 == i:		
			begintime = time.time()
			collection.insert(l)
			endtime = time.time()
			# dbsize = collection.count()
			signal.insert({'collectionName': 'th_trade_right','dbsize':collection.count(),"insertNum":10000, 'begintime':begintime, 'endtime':endtime , 'span':endtime - begintime})
			l = []
			i = 0

		#collection.insert(d)
		# print d

	# print "list", l
	if len(l) > 0:
		begintime = time.time()
		collection.insert(l)
		endtime = time.time()
		signal.insert({'collectionName': 'th_trade_right','dbsize':collection.count(),"insertNum":len(l), 'begintime':begintime, 'endtime':endtime , 'span':endtime - begintime})
	print len(l)

	cursor.close()
	con.close()

	timeDone = time.time()
	
	print 'insert span:', timeDone - timeFetch

	#print(orcl.Date(2015,3,13))

	# '''