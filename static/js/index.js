const Menu_mobile = document.getElementById('menu_nav_mobile')

Menu_mobile.addEventListener('click', animarMenu)

function animarMenu(){
    Menu_mobile.classList.toggle('menu_mobile_ativo');
}

var slide_ = document.querySelector('manual_btn')
var conteudo = 1

document.getElementById('slide_1').checked = true

setInterval(() => {
    proximaImg()
}, 5000)

function proximaImg(){
    conteudo++

    if(conteudo > 3){
        conteudo = 1
    }

    document.getElementById('slide_'+conteudo).checked = true
}

const dias = document.getElementById("dias")
const horas = document.getElementById("horas");
const minutos = document.getElementById("minutos");
const segundos = document.getElementById("segundos");
const data = document.currentScript.dataset
const live = data.live

console.log(live)

function tempo(){
    const relogio_dt = new Date(live);
    const hoje = new Date();
    //console.log(relogio_dt)
    //console.log(hoje)

    const totalSegundos = (relogio_dt - hoje) / 1000;

    const dy = Math.floor(totalSegundos / 3600 / 24);
    const hours = Math.floor(totalSegundos / 3600) % 24;
    const mins = Math.floor(totalSegundos / 60) % 60
    const sgs = Math.floor(totalSegundos) % 60

    dias.innerHTML = formatar_time(dy)
    horas.innerHTML = formatar_time(hours);
    minutos.innerHTML = formatar_time(mins);
    segundos.innerHTML = formatar_time(sgs);

    dias.innerHTML = fim_time(dy)
    horas.innerHTML = fim_time(hours);
    minutos.innerHTML = fim_time(mins);
    segundos.innerHTML = fim_time(sgs);
}

function formatar_time(time){
    return time < 10 ? `0${time}`: time;
}

function fim_time(time){
    return time <= 0 ? `0`: time;
}

tempo();

setInterval(tempo, 1000);

ScrollReveal({
    reset: true,
    distance: '60px',
    duration: 1000,
});

ScrollReveal().reveal('.activate', {origin: 'left'});