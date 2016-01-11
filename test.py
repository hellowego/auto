# -*-coding=utf8-*-


import datetime
import time

class Test():
	
	@classmethod
	def time2Stamp(cls):
		# 今天的日期
		today = datetime.date.today()
		print today
		print today.timetuple()
		
		# 今天日期的时间戳 mktime 输入参数struct_time对象 返回时间戳
		todayStamp =int(time.mktime(today.timetuple())) 
		print todayStamp
		
		# 当前时间的时间戳
		now = int(time.time())
		print now
		print now - todayStamp - 3600*24
		print (now - todayStamp)/3600
		
		# localtime  返回struct_time对象
		t = time.localtime(todayStamp)
		# strftime 参数t是一个struct_time对象 返回字符串
		timeStr = time.strftime('%Y-%m-%d %H:%M', t)
		print timeStr
		print t
		
		# 返回struct_time对象
		t1 = time.gmtime(now)
		print t1


if __name__ == "__main__":
	Test.time2Stamp()
	
	

