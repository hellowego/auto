#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
#

# import handlers.mainHandler
from tornado.web import RequestHandler, Application, url
from handlers.main_handler import IndexHandler
from handlers.account_handler import RegisterHandler, CheckUsernameHandler, CheckEmailHandler, LoginHandler, LogoutHandler, SettingHandler, ValidUsernameHandler
from handlers.exploreHandler import ExploreHandler
from handlers.questionHandler import QuestionHandler, AnswerAddHandler, AnswerVoteHandler, SaveAnswerComment, GetAnswerComment
from handlers.profileHandler import ProfileHandler
from handlers.profileHandler import FollowPeopleHandler
from handlers.questionHandler import SearchTopicHandler
from handlers.publishHandler import PublishQuestionHandler
from handlers.submitHandler import SubmitHandler, SubmitLinkHandler
from handlers.ajaxHandler import VoteHandler
from handlers.captchaHandler import CaptchaHandler
from handlers.testHandler import TestHandler



urls = [
	url(r'/', ExploreHandler),
	(r"/account/register", RegisterHandler),
	(r"/account/login", LoginHandler),
	(r"/account/logout", LogoutHandler),
	(r"/account/setting", SettingHandler),
	# 验证码
	(r"/account/captcha/([^/]+)", CaptchaHandler),
	(r"/check_username", CheckUsernameHandler),
	(r"/valid_username", ValidUsernameHandler),
	(r"/check_email", CheckEmailHandler),
	(r"/explore", ExploreHandler),

	# 
	(r"/submit", SubmitHandler),
	(r"/submit/save", SubmitLinkHandler),
	
	# (r"/question/([^/]+)", QuestionHandler),
	(r"/question/([0-9]$)", QuestionHandler),
	(r"/profile/(.*)", ProfileHandler),

	(r"/test", TestHandler),


	# ajax handler
	(r"/ajax/vote", VoteHandler),
	(r"/ajax/save_answer", AnswerAddHandler),
	(r"/question/ajax/answer_vote/", AnswerVoteHandler),
	(r"/question/ajax/save_answer_comment/([^/]+)", SaveAnswerComment),
	(r"/question/ajax/get_answer_comments/([^/]+)", GetAnswerComment),
	(r"/search/ajax/search/", SearchTopicHandler),
	(r"/publish/ajax/publish_question/", PublishQuestionHandler),


	(r"/follow/ajax/follow_people/", FollowPeopleHandler),

	]



if __name__ == "__main__":
	print 'hi'



