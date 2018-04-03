var solucionIndex = 0;

$( document ).ready(function() {
  limpiar();
  $("#botonSolucion").text("Solución");
});

function sleep(milliseconds) { 
        var start = new Date().getTime(); 
        for (var i = 0; i < 1e7; i++) { 
                if ((new Date().getTime() - start) > milliseconds){ break; } 
        } 
} 

function solucion(){


	if (juego.length == 0){
		alert("Recuerde ejecutar el codigo Python primero, luego de eso favor refrescar");
	}

	else {

		if (solucionIndex == juego.length) {
			solucionIndex = 0;
		}
		
		solucionAux(juego[solucionIndex]);
		solucionIndex++;
  		
	}
}

function solucionAux(ruta){
for (var i = 0; i < ruta.length; i++) {
    setTimeout((function(i) {
        return function() {
            var cpos = ruta[i];
            limpiar();
			dibujar(cpos);
            
        }
    })(i), i * 2000);
}

}




function dibujar(escenario){
	
	dibujarMisioneros(escenario[0][0],escenario[1][0]);
	dibujarCanibales(escenario[0][1],escenario[1][1]);

	if (escenario[0][2] == 1){
		$("#balIzq").attr("src","img/balza.png");
	}
	else{
		$("#balDer").attr("src","img/balza.png");
	}
}

function dibujarMisioneros(cantidadIzq, cantidadDer){

	var i = 1;
	while (i <= cantidadIzq) {
		$("#misIzq"+i.toString()).attr("src","img/misionero.png");
		i++;
	}

	i = 1;
	while (i <= cantidadDer) {
		$("#misDer"+i.toString()).attr("src","img/misionero.png");
		i++;
	}
	
}

function dibujarCanibales(cantidadIzq, cantidadDer){

	var i = 1;
	while (i <= cantidadIzq) {
		$("#canIzq"+i.toString()).attr("src","img/canibal.png");
		i++;
	}

	i = 1;
	while (i <= cantidadDer) {
		$("#canDer"+i.toString()).attr("src","img/canibal.png");
		i++;
	}
	
}


function limpiar(){

	$("#misIzq1").attr("src","img/rosadocielo.png");
	$("#misIzq2").attr("src","img/rosadocielo.png");
	$("#misIzq3").attr("src","img/rosadocielo.png");
	$("#canIzq1").attr("src","img/rosadocielo.png");
	$("#canIzq2").attr("src","img/rosadocielo.png");
	$("#canIzq3").attr("src","img/rosadocielo.png");
	$("#balIzq").attr("src","img/rosadocielo.png");
	$("#misDer1").attr("src","img/rosadocielo.png");
	$("#misDer2").attr("src","img/rosadocielo.png");
	$("#misDer3").attr("src","img/rosadocielo.png");
	$("#canDer1").attr("src","img/rosadocielo.png");
	$("#canDer2").attr("src","img/rosadocielo.png");
	$("#canDer3").attr("src","img/rosadocielo.png");
	$("#balDer").attr("src","img/rosadocielo.png");
	

} 



