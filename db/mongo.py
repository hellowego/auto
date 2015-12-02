#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
#

import pymongo

if __name__ == "__main__":
	print 'hi'

	client = pymongo.MongoClient()
	db = client.test
	collection = db.person
	obj = collection.find()[0]
	print obj
	print obj["name"], '  age: ', obj["age"]

