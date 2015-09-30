#!/usr/bin/env python
#-*- coding: UTF-8 -*- 


import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    """
    do some your base things
    """


class IndexHandler(BaseHandler):
    def get(self):
        welcome = "Hello,Torngas!"
        self.render("index.html", welcome=welcome)
