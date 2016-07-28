var AUTO = 
{
	// 赞成投票
	agree_vote: function(selector, user_name, link_id)
	{
		// 状态未投票
		if($(selector).parent().hasClass("unvoted")){
			$(selector).removeClass('up').addClass('upmod');
			$(selector).parent().addClass('likes').removeClass('unvoted');

			

			// 票数增加
			$.post("/ajax/vote",{id:link_id, value:"unvoted2like"},
				function  () {					
				}
				
			);
		}
		// 状态为喜欢
		else if($(selector).parent().hasClass("likes")){
			$(selector).removeClass('upmod').addClass('up');
			$(selector).parent().addClass('unvoted').removeClass('likes');
			// 票数增加
			$.post("/ajax/vote",{id:link_id, value:"like2unvoted"},
				function  () {					
				}
				
			);
		}
		// 状态为dislike
		else if($(selector).parent().hasClass("dislikes")){
			$(selector).removeClass('up').addClass('upmod');
			$(selector).parent().addClass('likes').removeClass('dislikes');
			$(selector).parent().find("i.downmod").removeClass('downmod').addClass('down');
			// 票数增加
			$.post("/ajax/vote",{id:link_id, value:"dislike2like"},
				function  () {					
				}
				
			);
		}

		
	},

	disAgree_vote: function(selector, user_name, link_id)
	{
		// 状态未投票
		if($(selector).parent().hasClass("unvoted")){
			$(selector).removeClass('down').addClass('downmod');
			$(selector).parent().addClass('dislikes');
			$(selector).parent().removeClass('unvoted');
			// 票数增加
			$.post("/ajax/vote",{id:link_id, value:"unvoted2dislike"},
				function  () {					
				}
				
			);
		}
		// 状态为喜欢
		else if($(selector).parent().hasClass("likes")){
			$(selector).removeClass('down').addClass('downmod');
			$(selector).parent().removeClass('likes').addClass('dislikes');
			$(selector).parent().find("i.upmod").removeClass('upmod').addClass('up');	
			// 票数增加
			$.post("/ajax/vote",{id:link_id, value:"like2dislike"},
				function  () {					
				}
				
			);	
		}
		// 状态为dislike
		else if($(selector).parent().hasClass("dislikes")){
			$(selector).removeClass('downmod').addClass('down');
			$(selector).parent().removeClass('dislikes').addClass('unvoted');
			// 票数增加
			$.post("/ajax/vote",{id:link_id, value:"dislike2unvoted"},
				function  () {					
				}
				
			);
		}

		
	},

	// ajax提交callback
	ajax_processer: function (type, result)
	{
		alert('网络链接异常6');
	},


	ajax_post: function(formEl, processer, type) // 表单对象，用 jQuery 获取，回调函数名
	{

		

		var custom_data = {
			_post_type: 'ajax'
		};


		try{

			formEl.ajaxSubmit(
			{
				dataType: 'json',
				data: custom_data,
				success: function (result)
				{
					alert(result);
					// processer(type, result);
				},
				error: function (error)
				{
					
				}
			});

		}catch(e){
			alert('网络链接异常6');
		}

		

	}

};