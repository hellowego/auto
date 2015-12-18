#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
#

'''
select count(1) from th_trade_right where id like '01%';  57485594   1:03
select count(1) from th_trade_right ;   397937882  3:46
select min(dealtime) from th_trade_right;   2014/1/1  15:12
select max(dealtime) from th_trade_right;  2015/2/28 13:00:00  16:09
select max(inlisttime),min(inlisttime) from th_trade_right;  2015/3/1 2:06:35  2014/1/1 4:12:15  16:34
select substr(id,0,4), count(1) from th_trade_right group by substr(id,0,4);   3:02

'''

import cx_Oracle as orcl
import pymongo
import json
import time
import datetime
import collections
import gc

if __name__ == "__main__":
	'''
	dealdate 日期批次表，记录下一个要搬移的日期批次，搬移的总次数
	signal 记录每次插入mongodb的日志，插入量、开始时间、结束时间、消耗时间、所属的日期批次、插入后的数据量
	moverecord 记录每个日期批次搬移数目和时间 
	th_trade_right 消费记录 
	
	'''
	
	username = "uopsett_b_sz"
	passwd = "uopsett"
	host = "172.16.128.250"
	port = "1521"
	sid = "szt"
	dsn = orcl.makedsn(host, port, sid)
	con = orcl.connect(username, passwd, dsn)

	# mongodb
	client = pymongo.MongoClient()
	#db = client.test
	db = client.one
	collection = db.th_trade_right
	signal = db.signal
	dbfetch = db.dbfetch
	dealdateCollection = db.dealdate
	
	# nj th_trade_right	
	column = ['ID','CARDNO','ASN','CARDTRADENO','SAMNO','POSNO','TRADEDATE','TRADETIME','PREMONEY','TRADEMONEY','BALUNITNO','BATCHNO','datebatchno']
		
	for i in range(12):
		# 获取要搬移数据的日期
		dealdateItme = db.dealdate.find_one()
		dealdateStr = dealdateItme["datebatchno"]		
		dotimes = dealdateItme["movetimes"]
		movetimes = int(dotimes) + 1
		

		print 'start deal: ' + dealdateStr
		timestart = time.time()
		

		# '''
		cursor = con.cursor()
		# sql = "SELECT * FROM th_trade_right where id like '010%'"
		sql = "SELECT ID,CARDNO,ASN,CARDTRADENO,SAMNO,POSNO,TRADEDATE,TRADETIME,PREMONEY,TRADEMONEY,BALUNITNO,BATCHNO FROM th_trade_right where id like \'" +  dealdateStr + "%\'"
		cursor.execute(sql)
		#result = cursor.fetchmany(2)
		result = cursor.fetchall()

		timeFetch = time.time()
		fetchspan = timeFetch - timestart
		
		count = cursor.rowcount
		
		l = []
		i = 0
		
		# 每1w条插入mongodb
		for row in result:
			#print(row)
			#row.append(dealdateStr)
			# d = collections.OrderedDict()
			d = collections.OrderedDict(zip(column,row))
			d['DATEBATCHNO'] = dealdateStr		
			
			# print d
			l.append(d)
			i += 1
			# 1w条批量插入
			if 10000 == i:		
				begintime = time.time()
				collection.insert(l)
				endtime = time.time()
				# dbsize = collection.count()
				#signal.insert({'collectionName': 'th_trade_right','datebatchno':dealdateStr,'dbsize':collection.count(),"insertNum":10000, 'begintime':begintime, 'endtime':endtime , 'span':endtime - begintime})
				l = []
				i = 0
			#collection.insert(d)
			# print d
		# print "list", l
		if len(l) > 0:
			begintime = time.time()
			collection.insert(l)
			endtime = time.time()
			#signal.insert({'collectionName': 'th_trade_right','datebatchno':dealdateStr,'dbsize':collection.count(),"insertNum":len(l), 'begintime':begintime, 'endtime':endtime , 'span':endtime - begintime})
		
		
		cursor.close()
		del result 
		gc.collect()
		
		
		timeDone = time.time()	
		insertspan = timeDone - timeFetch
		totalspan = timeDone - timestart
		
		#print(orcl.Date(2015,3,13))
		dbsize = collection.count()
		
		# 插入日期批次转移记录
		moverecord = collections.OrderedDict()
		moverecord['datebatchno'] = dealdateStr
		moverecord['count'] = count	
		moverecord['dbsize'] = dbsize
		moverecord['begintime'] = timestart
		moverecord['fetchtime'] = timeFetch
		moverecord['fetchspan'] = fetchspan
		moverecord['insertspan'] = insertspan
		moverecord['movedate'] = datetime.datetime.now()
		moverecord['status'] = '0'		
		db.moverecord.insert(moverecord)
		
		#db.moverecord.insert({'datebatchno':dealdateStr, 'count':count, 'movedate':datetime.datetime.now(),'begintime':timestart, 'fetchtime':timeFetch, 'fetchspan':fetchspan,'insertspan':insertspan, 'status':'0'})
		
		# 计算下一次搬移的数据的日期
		dealdate = datetime.datetime.strptime(dealdateStr, '%m%d')
		oneday = datetime.timedelta(days=1)
		nextday = dealdate + oneday
		nextdayStr = datetime.datetime.strftime(nextday, '%m%d') 
		print "done: "+dealdateStr+ " count: " + str(count) + ' dbsize: ' + str(dbsize) + " total span: " + str(totalspan)
		print "next date: " + nextdayStr
		# 更新处理日期
		db.dealdate.update({'datebatchno':dealdateStr}, {"$set":{'datebatchno':nextdayStr, 'updatetime':datetime.datetime.now(), 'movetimes':movetimes}})
	
	con.close()
		# '''