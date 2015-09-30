#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
#

# import handlers.mainHandler
from tornado.web import RequestHandler, Application, url
from handlers.main_handler import IndexHandler

urls = [
	url(r'/', IndexHandler, name='index'),
	]



if __name__ == "__main__":
	print 'hi'



