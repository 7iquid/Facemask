$(document).ready(function(){
  // let url2 = 'http://192.168.1.54:8000/api';
  let url2 = 'http://127.0.0.1:8000/api/'; 
    $('#mc1form').hide();
    $('#mc2form').hide();
    $('#mc3form').hide();

  setInterval(function(){
    $.ajax({
      url: url2,
      type: 'get',
      data: {
        'apikey':'machine_status'
      }, 
      success: function(response) {
        let machine_status1 = response[0].fields.machine_status;
        let machine_status2 = response[1].fields.machine_status;
        let machine_status3 = response[2].fields.machine_status;
        let machine1_date = response[0].fields.date;
        let machine2_date = response[1].fields.date;
        let machine3_date = response[2].fields.date;
        let pvDatem1 = DateEx(machine1_date);
        let pvDatem2 = DateEx(machine2_date);
        let pvDatem3 = DateEx(machine3_date);            
        let pm1 =DatehourEx(machine1_date);
        let pm2 =DatehourEx(machine2_date);
        let pm3 =DatehourEx(machine3_date);


        pvDatem1 = pvDatem1+' '+pm1;
        pvDatem2 = pvDatem2+' '+pm2;
        pvDatem3 = pvDatem3+' '+pm3;
 
        $('#mc1Timer').text(pvDatem1);
        $('#mc2Timer').text(pvDatem2);
        $('#mc3Timer').text(pvDatem3);

        if(machine_status1 == true)
          {
          $('#makina1').css("background-color", "#228B22");
          $('#mc1Status').text("Status: Machine Running");
          $('#mc1form').hide();
          } 
        else
          {
          $('#makina1').css("background-color", "#DC143C");
          $('#mc1Status').text("Status: Machine Down");
          $('#mc1form').show();
          };

        if(machine_status2 == true)
          {
          $('#makina2').css("background-color", "#228B22");
          $('#mc2Status').text("Status: Machine Running");
          $('#mc2form').hide();
          } 
        else
          {
          $('#makina2').css("background-color", "#DC143C");
          $('#mc2Status').text("Status: Machine Brakedown");
          $('#mc2form').show();
          };

        if(machine_status3 == true)
          {
          $('#makina3').css("background-color", "#228B22");
          $('#mc3Status').text("Status: Machine Running");
          $('#mc3form').hide();
          } 
        else
          {
          $('#makina3').css("background-color", "#DC143C");
          $('#mc3Status').text("Status: Machine Brakedown");
          $('#mc3form').show();
          };


      },
      error: function(XMLHttpRequest, textStatus, errorThrown) { 
      
      }       

      })
    },1000);




});
// end of interval funtion

function DateEx(machine1_date){

    var now = new Date();
    let befor = new Date(machine1_date);

    let month1 = now.getUTCMonth(); //months from 1-12
    let day1 = now.getUTCDate();
    let year1 = now.getUTCFullYear();

    let month2 = befor.getUTCMonth(); //months from 1-12
    let day2 = befor.getUTCDate();
    let year2 = befor.getUTCFullYear();

    let month3 = month1 -month2
    let day3 = day1 -day2
    let year3 = year1 -year2

    month3 =Math.abs(month3)
    day3 =Math.abs(day3)
    year3 =Math.abs(year3)

    return year3 + "/" + month3 + "/" + day3;
};



function DatehourEx(machine1_date){

  let pcDate =(Date.now() - Date.parse(machine1_date))/1000;
  var date = new Date(0);
  date.setSeconds(pcDate); // specify value for SECONDS here
  var timeString = date.toISOString().substr(11, 8);
    return timeString
};

$(document).ready(function(){
  setInterval(function(){

  },1000)


});


