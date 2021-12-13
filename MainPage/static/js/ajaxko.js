$(document).ready(function(){
	setInterval(function(){
		$.ajax({
			url: 'api/ajax',
			type: 'get',
			data: {machine_no:"1"},
			success: function(response) {
				console.log('ok na ata');
			}
			})
		},10000)




})