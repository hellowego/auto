#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
#

# import handlers.mainHandler
from tornado.web import RequestHandler, Application, url
from handlers.main_handler import IndexHandler
from handlers.account_handler import RegisterHandler, CheckUsernameHandler, CheckEmailHandler, LoginHandler, LogoutHandler
from handlers.exploreHandler import ExploreHandler
from handlers.questionHandler import QuestionHandler, AnswerAddHandler, AnswerVoteHandler



urls = [
	url(r'/', ExploreHandler),
	(r"/account/register", RegisterHandler),
	(r"/account/login", LoginHandler),
	(r"/account/logout", LogoutHandler),
	(r"/check_username", CheckUsernameHandler),
	(r"/check_email", CheckEmailHandler),
	(r"/explore", ExploreHandler),
	
	# (r"/question/([^/]+)", QuestionHandler),
	(r"/question/([0-9]$)", QuestionHandler),


	# ajax handler
	(r"/ajax/save_answer", AnswerAddHandler),
	(r"/question/ajax/answer_vote/", AnswerVoteHandler),
	]



if __name__ == "__main__":
	print 'hi'



