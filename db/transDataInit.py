#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
#

import cx_Oracle as orcl
import pymongo
import json
import time
import datetime

if __name__ == "__main__":

	# mongodb
	client = pymongo.MongoClient()
	#db = client.one
	db = client.test
	# collection = db.tf_f_cardrec
	collection = db.th_trade_right
	signal = db.signal
	dbfetch = db.dbfetch
	collection.drop()
	signal.drop()
	dbfetch.drop()
	db.dealdate.drop()
	db.dealdate.insert({'datebatchno':'0101', 'updatetime':datetime.datetime.now(), 'movetimes':'0'})
	db.moverecord.drop()
	

	
