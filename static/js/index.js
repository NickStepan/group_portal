const logo = document.getElementById('logo');
const logodiv = logo.querySelector('div');
const search = document.querySelector('search input');
const clear = document.getElementById('clear');


let animation = lottie.loadAnimation({
    container: logodiv,
    renderer: 'svg',  
    loop: false,     
    autoplay: false, 
    path: `${static}graphics/lottie/unitedflow.json`
});

animation.addEventListener('DOMLoaded', function() {
    let svgElement = animation.renderer.svgElement;

    if (svgElement) {
        svgElement.setAttribute("viewBox", "0 0 500 500"); 
        svgElement.setAttribute("width", "100%");         
        svgElement.setAttribute("height", "100%");      
    }
});

let isplaying = false;

animation.addEventListener('complete', function() {
    isplaying = false;
    animation.goToAndStop(0, true);
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