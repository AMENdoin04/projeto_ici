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