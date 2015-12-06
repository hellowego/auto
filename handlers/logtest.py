#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
#

# import logging

# import logging
# import logging.config
# import auto
# from auto import util
# import .. models.user_models
# from .. import user_models
# from . import getLogger
import sys
sys.path.append("..")
import util


if __name__ == "__main__":
	print 'hi'
	
	# logging.config.fileConfig("logger.config")
	# # logger = logging.getLogger("root")


	# logger = logging.getLogger("trace")
	# # logger = logging.getLogger("result")

	logger = util.getLogger()

	logger.debug('This is debug message')
	# logger.info('This is info message')
	# logger.warning('This is warning message')
