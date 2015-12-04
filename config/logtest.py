#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
#

import logging
import logging.config


if __name__ == "__main__":
	print 'hi'
	
	# logging.config.fileConfig("logging.config")
	# logger = logging.getLogger("root")


	# logger = logging.getLogger("trace")
	logger = logging.getLogger("result")

	logger.debug('This is debug message')
	logger.info('This is info message')
	logger.warning('This is warning message')
