var register = document.getElementById('div_sec');
var login = document.getElementById('div_prin');

function register() {
    if (register.classList.contains('animacionDivReg')){
        register.classList.remove('animacionDivReg');
        register.classList.add('animacionDivRegVuelta');
        register.style.opacity = 1;
        register.style.left = '36%';


    }
    else{
        register.classList.remove('animacionDivRegVuelta');
        register.classList.add('animacionDivReg');
        register.style.opacity = 0;
        register.style.left = '20%';
    }
}

function login() {
    if (login.classList.contains('animacionDivLog')){
        login.classList.remove('animacionDivLog');
        login.classList.add('animacionDivLogVuelta');
        login.style.opacity = 1;
        login.style.left = '36%';


    }
    else{
        login.classList.remove('animacionDivLogVuelta');
        login.classList.add('animacionDivLog');
        login.style.opacity = 0;
        login.style.left = '20%';
    }
}


