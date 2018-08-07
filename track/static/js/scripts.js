$(document).ready(function() {
	if($('div.base-toast').length > 0) {
		setTimeout(function() {
			$('div.base-toast').slideToggle(100);
		}, 1500);
	}
});