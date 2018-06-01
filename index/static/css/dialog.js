$("#dialog-form").on('submit', function(event){
        event.preventDefault();
        $.ajax({
        url: '/dialog/',
        type: 'POST',
        data: {dialogbox : $('#dialog-msg').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
                },
        
        success : function(json){
			$('#dialog-msg').val('');
                $('#send').attr('disabled', 'disabled');
			$('#dialog-list').append('<li class="text-right list-group-item"><small style="color:grey">~' + json.user + '</small><br><span style="font-size:25px">' + json.dialog + '</span><br><small style="color:grey">' + json.time + '</small></li>');
			if(document.getElementById('startconvo').disabled == true){
				$('#dialog-list').append('<li class="text-left list-group-item"><small style="color:grey">~Computer</small><br><span style="font-size:25px">' + json.dialog1 + '</span><br><small style="color:grey">' + json.time + '</small></li>');
			if(json.dialog1 == "Yupp! you found the number."){
				$('#startconvo').removeAttr('disabled');
}			
}
			var off=$('#down').offset();
			window.scrollBy(0, off.top);
        }
});
});

$("#startconvo-form").on('submit', function(event){
        event.preventDefault();
        var number= Math.floor(Math.random()*(101-1+1))+1;
        $.ajax({
        url: '/startconvo/',
        type: 'POST',
        data: {dialogue: "Guess a number between 1 and 101.",
                num: number,
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                user2name: "fromComputer",            
            },

        success: function(json){
                $('#dialog-msg').val('');
                $('#send').attr('disabled', 'disabled');
                $('#startconvo').attr('disabled', 'disabled');
                $('#dialog-list').append('<li class="text-left list-group-item"><small style="color:grey">~Computer</small><br><span style="font-size:25px">' + json.dialog + '</span><br><small style="color:grey">' + json.time + '</small></li>');
		var off=$('#down').offset();
			window.scrollBy(0, off.top);
        }
})
})

$(document).ready(function(){
	
	$('#send').attr('disabled', 'disabled');
	$('#dialog-msg').keyup(function(){
		if($(this).val() != ''){
			$('#send').removeAttr('disabled');
		}
		else{
			$('#send').attr('disabled', 'disabled');
		}
	}) ;
});

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
