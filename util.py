#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
#

import logging
import logging.config


def getLogger():
	logging.config.fileConfig("config/logger.config")
	logger = logging.getLogger("trace")

	return logger

