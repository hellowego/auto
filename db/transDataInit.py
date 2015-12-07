#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
#

import cx_Oracle as orcl
import pymongo
import json
import time

if __name__ == "__main__":
	

	# mongodb
	client = pymongo.MongoClient()
	db = client.one
	# collection = db.tf_f_cardrec
	collection = db.th_trade_right
	signal = db.signal
	dbfetch = db.dbfetch
	collection.drop()
	signal.drop()
	dbfetch.drop()
	

	
