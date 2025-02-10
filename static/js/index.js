const logo = document.getElementById('logo');
const logodiv = logo.querySelector('div');


let animation = lottie.loadAnimation({
    container: logodiv,
    renderer: 'svg',  
    loop: false,     
    autoplay: false, 
    path: `${static}graphics/lottie/unitedflow.json`,
    rendererSettings: {
        viewBox: '0 0 500 500'
    }
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
        animation.goToAndPlay(0, true);
    }
    
});