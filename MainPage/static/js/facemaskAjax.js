$(document).ready(function(){
  setInterval(function(){
    $.ajax({
      url: 'http://127.0.0.1:8000/api',
      type: 'get',
      data: {
        'apikey':'papa pogi'
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
          } 
        else
          {
          $('#makina1').css("background-color", "#DC143C");
          $('#mc1Status').text("Status: Machine Down");
          };

        if(machine_status2 == true)
          {
          $('#makina2').css("background-color", "green");
          $('#mc2Status').text("Status: Machine Running");
          } 
        else
          {
          $('#makina2').css("background-color", "red");
          $('#mc2Status').text("Status: Machine Brakedown");
          };

        if(machine_status3 == true)
          {
          $('#makina3').css("background-color", "green");
          $('#mc3Status').text("Status: Machine Running");
          } 
        else
          {
          $('#makina3').css("background-color", "red");
          $('#mc3Status').text("Status: Machine Brakedown");
          };


      },
 
      })
    },1000)




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

