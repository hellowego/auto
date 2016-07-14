var AUTO = 
{
	// 赞成投票
	agree_vote: function(selector, user_name, answer_id)
	{
		// 状态未投票
		if($(selector).parent().hasClass("unvoted")){
			$(selector).removeClass('up').addClass('upmod');
			$(selector).parent().addClass('likes').removeClass('unvoted');

			

			// 票数增加
			$.post("/ajax/vote",{id:1, value:"like"},
				function  () {
					// body...
					// alert('hi');
				}
				
			);
		}
		// 状态为喜欢
		else if($(selector).parent().hasClass("likes")){
			$(selector).removeClass('upmod').addClass('up');
			$(selector).parent().addClass('unvoted').removeClass('likes');
		}
		// 状态为dislike
		else if($(selector).parent().hasClass("dislikes")){
			$(selector).removeClass('up').addClass('upmod');
			$(selector).parent().addClass('likes').removeClass('dislikes');
			$(selector).parent().find("i.downmod").removeClass('downmod').addClass('down');
		}

		
	},

	disAgree_vote: function(selector, user_name, answer_id)
	{
		// 状态未投票
		if($(selector).parent().hasClass("unvoted")){
			$(selector).removeClass('down').addClass('downmod');
			$(selector).parent().addClass('dislikes');
			$(selector).parent().removeClass('unvoted');
		}
		// 状态为喜欢
		else if($(selector).parent().hasClass("likes")){
			$(selector).removeClass('down').addClass('downmod');
			$(selector).parent().removeClass('likes').addClass('dislikes');
			$(selector).parent().find("i.upmod").removeClass('upmod').addClass('up');		
		}
		// 状态为dislike
		else if($(selector).parent().hasClass("dislikes")){
			$(selector).removeClass('downmod').addClass('down');
			$(selector).parent().removeClass('dislikes').addClass('unvoted');
		}

		
	}

};