controles = document.getElementById('controles');
sensores = document.getElementById('sensores');
arduino = document.getElementById('arduino');
conectedArd = document.getElementById('conectedArd');
iniciarArduino = document.getElementById('iniciarArduino');

getParams();

function conectaArd(){
	 value = document.getElementById('conectaArd').checked;
	 $.ajax({
                contentType: 'application/json;charset=UTF-8',
				type: 'POST',
                dataType: 'json',
                url: '/conectaArd',
                async: true,
                data: JSON.stringify(value),
                success: function(result) {
					if(result == 'True'){
						icArduinoConnected();
					}
                    else{
                        alert(result);
                        document.getElementById('conectaArd').checked = false;
                    }
                },
        error: function (result) {
            console.log(result);
        }
            });
}

function iniciarSensores(){
    value = document.getElementById('connectSensores').checked;
    $.ajax({
               contentType: 'application/json;charset=UTF-8',
               type: 'POST',
               dataType: 'json',
               url: '/connectSensores',
               async: true,
               data: JSON.stringify(value),
               success: function(result) {
                   if(result == 'true'){
                       document.getElementById('connectSensores').setAttribute ('disabled','disabled')
                   }
               },
       error: function (result) {
           console.log(result);
       }
           });
}

function cancela(){
    value = document.getElementById('btnCancela').checked;
    $.ajax({
               contentType: 'application/json;charset=UTF-8',
               type: 'POST',
               dataType: 'json',
               url: '/cancela',
               async: true,
               data: JSON.stringify(value),
               success: function(result) {
                   if(result == 'true'){
                       console.log("Cancela Alterada");
                   }
               },
       error: function (result) {
           console.log(result);
       }
           });
}


function icArduinoConnected(){
	controles.style.display = "block";
	sensores.style.display = "block";
	conectedArd.style.display = "block";
    document.getElementById('conectaArd').setAttribute ('disabled','disabled');
}

function getParams(){
    $.get("/getParam", function(resultado){
        data = JSON.parse(resultado)
        console.log(resultado);
        if(data['arduinoConectado']==1){
            document.getElementById('conectaArd').checked = true;
            icArduinoConnected();
        }
        if(data['sensoresIniciados']==1){
            document.getElementById('connectSensores').checked = true;
            document.getElementById('connectSensores').setAttribute ('disabled','disabled')
        }
        if(data['icCancelaLiberada']==1){
            console.log(data['icCancelaLiberada']);
            document.getElementById('btnCancela').checked = true;
        }
   })
}


async function getVagas(){
    $.get("/getVagas", function(resultado){
        data = JSON.parse(resultado)
        if(data['icVaga1'] == 1){
            document.getElementById('v1').style.backgroundColor = 'red';
            document.getElementById('v1diponivel').style.display = 'none';
            document.getElementById('v1indisponivel').style.display = 'block';
        }
        else{
            document.getElementById('v1').style.backgroundColor = 'green';
            document.getElementById('v1diponivel').style.display = 'block';
            document.getElementById('v1indisponivel').style.display = 'none';
        }

        if(data['icVaga2'] == 1){
            document.getElementById('v2').style.backgroundColor = 'red';
            document.getElementById('v2diponivel').style.display = 'none';
            document.getElementById('v2indisponivel').style.display = 'block';
        }
        else{
            document.getElementById('v2').style.backgroundColor = 'green';
            document.getElementById('v2diponivel').style.display = 'block';
            document.getElementById('v2indisponivel').style.display = 'none';
        }

        if(data['icVaga3'] == 1){
            document.getElementById('v3').style.backgroundColor = 'red';
            document.getElementById('v3diponivel').style.display = 'none';
            document.getElementById('v3indisponivel').style.display = 'block';
        }
        else{
            document.getElementById('v3').style.backgroundColor = 'green';
            document.getElementById('v3diponivel').style.display = 'block';
            document.getElementById('v3indisponivel').style.display = 'none';
        }
   })
  // setTimeout(getVagas(), 1000); 
}

window.setInterval(function() {
    getVagas();
  }, 1000);