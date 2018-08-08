$(document).ready(function() {
	if($('div.base-toast').length > 0) {
		setTimeout(function() {
			$('div.base-toast').slideToggle(100);
		}, 1500);
	}

	function ajaxSubmit($form, successCallback, errorCallback) {
		$form.find('input[name=assigned_to]').val(1);
		$.ajax({
			url: $form.attr('action'),
			type: 'POST',
			dataType: 'json',
			cache: false,
			headers: { "X-CSRFToken": $form.attr('data-csrf-token') },
			data: $form.serialize(),
			success: function(result) {
				successCallback(result);
			},
			error: function(result) {
				errorCallback(result);
			}
		});
	}

	$('article.issue form.add_comment_form input').keypress(function(e) {
		if(e.which != 10 && e.which != 13) return;
		if($(this).val().trim() == '') return false;
		$form = $(this).parents('form');
		if($form.hasClass('preventEvent')) return false;
		$form.addClass('preventEvent');
		ajaxSubmit($form, function(result) {
			$form.removeClass('preventEvent');
			$form.find('input[name=content]').val('');
			$('<li class="comment clearfix">\
								<a href="#profilepage" class="floatL">\
								<div class="author clearfix">\
								<div class="profile_pic floatL">\
								<img class="profile_pic" src="' + (result.pic.length > 0? result.pic : '/static/image/assets/profile_img_placeholder.png') + '" />\
								</div>\
								<div class="team_name floatL">\
								' + result.team_name + ' </div>\
								<div class="name floatL">\
								' + result.author+ '님</div></div></a>\
						<div class="comment floatL">' + result.content + '</div><div class="created_at">방금</div></li>').insertBefore($form);
			
		}, function(result) {
			$form.removeClass('preventEvent');
		});
		return false;
	});

	$('article.issue form.ajax_form a.btn_submit').click(function() {
		$form = $(this).parents('form');
		ajaxSubmit($form);
	});
});