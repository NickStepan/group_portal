const logo = document.getElementById('logo');
const logodiv = logo.querySelector('div');
const search = document.querySelector('search input');
const clear = document.getElementById('clear');
const menu = document.getElementById('menu');


let animation = lottie.loadAnimation({
    container: logodiv,
    renderer: 'svg',  
    loop: false,     
    autoplay: false, 
    path: `${static}graphics/lottie/unitedflow.json`
});

let menuanim = lottie.loadAnimation({
    container: menu,
    renderer: 'svg',  
    loop: false,     
    autoplay: false, 
    path: `${static}graphics/lottie/menu-f.json`
});

let menuanim2 = lottie.loadAnimation({
    container: menu,
    renderer: 'svg',   
    loop: false,     
    autoplay: false, 
    path: `${static}graphics/lottie/menu-b.json`
});

animation.addEventListener('DOMLoaded', () => {
    let svgElement = animation.renderer.svgElement;

    if (svgElement) {
        svgElement.setAttribute("viewBox", "0 0 500 500"); 
        svgElement.setAttribute("width", "100%");         
        svgElement.setAttribute("height", "100%");      
    }
});

menuanim2.addEventListener('DOMLoaded', () => {
    let svgElement = menuanim2.renderer.svgElement;
    if (svgElement) {
        svgElement.style.display = 'none';
    }
});

let isplaying = false;

animation.addEventListener('complete', function() {
    isplaying = false;
    animation.goToAndStop(0, true);
});

menuanim.addEventListener('complete', () => {
    isplayingmenu = false;
    opened = true;
    menuanim.renderer.svgElement.style.display = 'none';
    menuanim2.renderer.svgElement.style.display = 'block';
    menuanim2.goToAndStop(0, true);
});

menuanim2.addEventListener('complete', () => {
    isplayingmenu = false;
    opened = false;
    menuanim.renderer.svgElement.style.display = 'block';
    menuanim2.renderer.svgElement.style.display = 'none';
    menuanim.goToAndStop(0, true);
});

logo.addEventListener('mouseenter', () => {
    if (!isplaying) {
        isplaying = true;
        animation.play();
    }
    
});

search.addEventListener('focus', () => {
    search.placeholder = 'Пошук...'
});

search.addEventListener('blur', () => {
    search.placeholder = '\uE000'
});

clear.addEventListener('click', () => {
    search.value = '';
    search.focus();
});

let opened = false;
let isplayingmenu = false;

menu.addEventListener('click', () => {
    if (!isplayingmenu) {
        isplayingmenu = true;
        if (!opened) {
            menuanim.play()
        } else {
            menuanim2.play();
        }
    }
});
