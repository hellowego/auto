var AUTO = 
{
	// 赞成投票
	agree_vote: function(selector, user_name, answer_id)
	{
		$(selector).removeClass('up');
		$(selector).addClass('upmod');
	}

};