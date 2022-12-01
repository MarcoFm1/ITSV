var titulo = document.getElementById('titulo');
var parrafo = document.getElementById('parrafo');
var boton = document.getElementById('boton');


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





    if (boton.classList.contains('animacionBotonIda')){
        boton.classList.remove('animacionBotonIda');
        boton.classList.add('animacionBotonVuelta');
        boton.style.top = '57%';
    }
    else{
        boton.classList.add('animacionBotonIda');
        boton.classList.remove('animacionBotonVuelta');
        boton.style.top = '92%';
    }
}