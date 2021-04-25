
function telaResultadoCalculo2Grau(){//Exibe a resuloção das raízes da função calcular2Grau() na tela.
  let valorRaiz = calcular2Grau();
  var resolucaoRaiz = document.getElementById('resultado-raizes');
  resolucaoRaiz.innerText = valorRaiz;

  let valorMaxMin = maximo_minimo();
  var resolucaoMaxMin = document.getElementById('resultado-maxmin');
  resolucaoMaxMin.innerText = valorMaxMin;

  let valorCompleto = completaOuIncompleta();
  var resolucaoCompleto = document.getElementById('resultado-comincom');
  resolucaoCompleto.innerText = valorCompleto;

  

  parabola()
}


function calculoRaiz(numero) {//Função que calcula a raíz quadrada de um número. 

  var divisorRaiz = 1, calcDiv = 0;
  for (var i = 0; i <= numero; i++) {
      calcDiv = numero / divisorRaiz;
      divisorRaiz = (calcDiv + divisorRaiz) / 2;
  }
  return divisorRaiz;
}

function calcular2Grau(){//Calcula os X's da função
  var a = document.getElementById('adeX').value;
  var b = document.getElementById('bdeX').value;
  var c = document.getElementById('cdeX').value;

  var delta = ((b**2)-(4*a*c));
  if (delta < 0 ){
    return 'Delta < 0 não há resultado em R.';
  }
  else{
    var x2 = (((b)*(-1)) + calculoRaiz(delta))/(2*a);
    var x1 = (((b)*(-1)) - calculoRaiz(delta))/(2*a);
    x1 == Infinity || x1==-Infinity? x1 = "Vazio, não há raíz.": x1 = x1.toFixed(2);
    x2 == Infinity || x2==-Infinity? x2 = "Vazio, não há raíz.": x2 = x2.toFixed(2);
    
    return "X1 é " + x1 +" X2 é " + x2;
  }
  
}

function parabola(){//Destaca a horientação da parabola de acordo com o valor de A.
  var a = document.getElementById('adeX').value;
  var baixo = document.getElementById('baixo');
  a <0? baixo.innerHTML= "<p>A negativo, logo: </p><div id='parabola-cima'></div>": baixo.innerHTML="<p>A positivo, logo:</p><div id='parabola-baixo'></div>";
  
}

function maximo_minimo(){//Rertona os pontos máximo e mínimo com relação ao valor de A.
  var a = document.getElementById('adeX').value;
  var b = document.getElementById('bdeX').value;
  var c = document.getElementById('cdeX').value;

  var delta = ((b**2)-(4*a*c));
  var result = 0;
  

  var verticeX = (b*-1)/(2*a)
  var verticeY = (delta * -1)/(4*a);

  return "Vertice (" + verticeX.toFixed(2) +", " + verticeY.toFixed(2) + ")";

  
}

function completaOuIncompleta(){
  var a = document.getElementById('adeX').value;
  var b = document.getElementById('bdeX').value;
  var c = document.getElementById('cdeX').value;
  var resultado = "";

  b != 0 && c!=0 ? resultado = "Completa": resultado = "Incompleta";
  return  resultado;
}


function mostrarLista(num){
  var lista = ['funcionalidades-dd', 'raizes-dd', 'pontos-dd', 'parabola-dd', 'comincomp-dd'];
  var elementos = document.getElementsByClassName(lista[num]);
  if (elementos[0].classList.contains('slide-fwd-center')){
    for (var i =0; i< elementos.length; i++){
      elementos[i].classList.remove('slide-fwd-center');
    }

  }
  else{
  
  for (var i =0; i< elementos.length; i++){
    elementos[i].classList.add('slide-fwd-center');
  }
  }
}