#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import unittest


from account_handler import RegisterHandler

class account_handler_test(unittest.TestCase):
	
	
	def setUp(self):
		self.tclass = RegisterHandler('hi', 'hi')
		# pass

	#退出清理工作
	def tearDown(self):
		pass


	def test_check(self):
		# bl = account_handler.RegisterHandler.check('hi', "hello@gmail.com", '111')
		self.assertEqual(self.tclass.check('hi', "hello@gmail.com", '111'), False)
		print 'hi'




if __name__ == "__main__":
	unittest.main()
