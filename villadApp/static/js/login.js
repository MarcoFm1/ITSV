var register = document.getElementById('titulo');
var login = document.getElementById('parrafo');
var botonLog = document.getElementById('');
var botonReg = document.getElementById('btn_reg')
var Dha = document.getElementById('a_dha')

function animacion(){
    if (titulo.classList.contains('animacionTituloIda')){
        titulo.classList.remove('animacionTituloIda');
        titulo.classList.add('animacionTituloVuelta');
        titulo.style.top = '43%';
        titulo.style.left = '50%';
        titulo.style.fontSize = '40px';
    }
    else{
        titulo.classList.add('animacionTituloIda');
        titulo.classList.remove('animacionTituloVuelta');
        titulo.style.top = '5%';
        titulo.style.left = '10%';
        titulo.style.fontSize = '20px';
    }



    if (parrafo.classList.contains('opacidadParrafoIda')){
        parrafo.classList.remove('opacidadParrafoIda');
        parrafo.classList.add('opacidadParrafoVuelta');
        parrafo.style.opacity = '0.0';
        parrafo.style.fontSize = '1px';
    }
    else{
        parrafo.classList.add('opacidadParrafoIda');
        parrafo.classList.remove('opacidadParrafoVuelta');
        parrafo.style.opacity = '1.0';
        parrafo.style.fontSize = '30px';
    }
}
