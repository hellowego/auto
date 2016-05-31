#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
#


import os.path
import subprocess
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import urls
from tornado.options import define, options
from handlers.questionHandler import QuestionModule
from handlers.uiModules import AnswerModule
from handlers.uiModules import FollowListModule, LinkModule


define("port", default=8888, help="run on the given port", type=int)


class Application(tornado.web.Application):
	def __init__(self):
		handlers = urls.urls

		settings = dict(
			blog_title=u"auto Blog",
			template_path=os.path.join(os.path.dirname(__file__), "templates"),
			static_path=os.path.join(os.path.dirname(__file__), "static"),
			ui_modules={"Question": QuestionModule, "Answer": AnswerModule, "FollowList": FollowListModule, "LinkModule":LinkModule},
			xsrf_cookies=False,
			cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
			login_url="/auth/login",
			debug=True,
		)

		super(Application, self).__init__(handlers, **settings)

def main():
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
	main()
