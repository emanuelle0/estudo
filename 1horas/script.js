var d = new Date();
var hora = d.getHours();
var minutos = d.getMinutes();
var segundos = d.getSeconds();

var horaAtual =  hora + ":" + minutos + ":" + segundos ;



var tempo = document.getElementById("tempo");
tempo.innerHTML += horaAtual;

