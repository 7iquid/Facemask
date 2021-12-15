$(document).ready(function(){
	setInterval(function(){
		$.ajax({
			url: 'api/',
			type: 'get',
			data: {
				machine_no1:"1",
				machine_no2:"2",
				machine_no3:"3",
			},
			success: function(response) {
				let machine_status1 = response.machine_status1
				let machine_status2 = response.machine_status2
				let machine_status3 = response.machine_status3

				// console.log('ok na ata',response.machine_status);
				

				if(machine_status1 == true)
					{
					$('#makina1').css("background-color", "green");
					} 
				else
					{
					$('#makina1').css("background-color", "red");
					};

				if(machine_status2 == true)
					{
					$('#makina2').css("background-color", "green");
					} 
				else
					{
					$('#makina2').css("background-color", "red");
					};

				if(machine_status3 == true)
					{
					$('#makina3').css("background-color", "green");
					} 
				else
					{
					$('#makina3').css("background-color", "red");
					};


			}
			})
		},1000)




})