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
	# Test.time2Stamp()

	result = '''
	<ul>
		<li>
			<a class="aw-user-name" href="http://wenda.wecenter.com/people/seosns" data-id="8884"><img src="http://wenda.wecenter.com/uploads/avatar/000/00/88/84_avatar_min.jpg" alt="" /></a>
		
			<div>
				<p class="clearfix">
				
								<span class="pull-right">
											<a href="javascript:;" onclick="if ($(this).parents('.aw-comment-box').find('form textarea').val() == $(this).parents('.aw-comment-box').find('form textarea').attr('placeholder')){$(this).parents('.aw-comment-box').find('form textarea').val('');};$(this).parents('.aw-comment-box').find('form').show().find('textarea').focus();$(this).parents('.aw-comment-box').find('form textarea').insertAtCaret('@seosns:');$.scrollTo($(this).parents('.aw-comment-box').find('form'), 300, {queue:true});$(this).parents('.aw-comment-box').find('textarea').focus();">回复</a>				</span>
							
				<a href="http://wenda.wecenter.com/people/seosns" class="aw-user-name author" data-id="8884">seosns</a> • <span>2015-04-17 21:45</span>
				</p>
				<p class="clearfix">谢谢你的肯定和建议，会陆续完善的</p>
			</div>
		</li>
	</ul>
	'''

	a = '		hi, /%s, hello %s' 
		
	b = a %('jack', 'tom')
	print b
	
	

