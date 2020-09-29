const botonEsc = document.querySelector('.boton-esconder');

botonEsc.addEventListener('click',function(){
    document.getElementById('barra').classList.toggle('active');
});