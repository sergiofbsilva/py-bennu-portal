$(document).ready(function () {
			var menuendpoint = "http://ashtray.ist.utl.pt:8001/menu/";
			var remote_url = menuendpoint + window.location.hostname

			var head_url = menuendpoint + "head/" + window.location.hostname
			
			var head_html = $.ajax( {
						type: "GET",
						url : head_url,
						async: false}).responseText;
			
			head_div = document.createElement('div');
    		head_div.innerHTML = head_html;
    		$('head').append(head_div.firstChild);

    		
    		var target_html = $.ajax({
				type: "GET",
				url: remote_url,
				async: false
				}).responseText;
	
    		body_html = $('body')[0].innerHTML;
    		div = document.createElement('div');
    		div.innerHTML = target_html;
    		
    		$(div).find("#content")[0].innerHTML = body_html;
    		$('body')[0].innerHTML = div.innerHTML;
});