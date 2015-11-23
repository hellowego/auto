#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
#

# import handlers.mainHandler
from tornado.web import RequestHandler, Application, url
from handlers.main_handler import IndexHandler
from handlers.account_handler import RegisterHandler, CheckUsernameHandler, CheckEmailHandler, LoginHandler, OcxTestHandler
from handlers.exploreHandler import ExploreHandler
from handlers.questionHandler import QuestionHandler



urls = [
	url(r'/', IndexHandler, name='index'),
	(r"/account/register", RegisterHandler),
	(r"/account/login", LoginHandler),
	(r"/check_username", CheckUsernameHandler),
	(r"/check_email", CheckEmailHandler),
	(r"/explore", ExploreHandler),
	(r"/ocxtest", OcxTestHandler),
	(r"/question/([^/]+)", QuestionHandler),
	]



if __name__ == "__main__":
	print 'hi'



