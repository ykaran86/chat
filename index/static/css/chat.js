$('#chat-form').on('submit', function(event){
	event.preventDefault();
	$.ajax({
		url: '/post/',
		type: 'POST',
		data: {msgbox : $('#chat-msg').val(),
			csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()			
			},

		success : function(json){
			$('#chat-msg').val('');
			$('#msg-list').append('<li class="text-right list-group-item"><small style="color:grey">~' + json.user + '</small><br><span style="font-size:25px">' + json.msg + '</span><br><small style="color:grey">' + json.time + '</small></li>');
			var off=$('#down').offset();
			window.scrollBy(0, off.top);
			var chatlist = document.getElementById('msg-list-div');
			chatlist.scrollTop=chatlist.scrollHeight;
			
		}
	});
});

function getMessages(){
	if(!scrolling){
		$.get('/messages/', function(messages){
			$('#msg-list').html(messages);
			var chatlist = document.getElementById('msg-list-div');
			chatlist.scrollTop = chatlist.scrollHeihgt;
		});
	}
	scrolling = false;
}
var scrolling = false;
$(function(){
	$('#msg-list-div').on('scroll', function(){
		scrolling=true;
	});
	refreshTimer = setInterval(getMessages, 2500);
});2

$(document).ready(function(){
	
	$('#send').attr('disabled', 'disabled');
	$('#chat-msg').keyup(function(){
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
