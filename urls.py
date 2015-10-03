#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
#

# import handlers.mainHandler
from tornado.web import RequestHandler, Application, url
from handlers.main_handler import IndexHandler
from handlers.account_handler import RegisterHandler, CheckUsernameHandler, CheckEmailHandler



urls = [
	url(r'/', IndexHandler, name='index'),
	(r"/register", RegisterHandler),
	(r"/check_username", CheckUsernameHandler),
	(r"/check_email", CheckEmailHandler),
	]



if __name__ == "__main__":
	print 'hi'



