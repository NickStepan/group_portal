const logo = document.getElementById('logo');
const logodiv = logo.querySelector('div');
const search = document.querySelector('search input');
const clear = document.getElementById('clear');
const menu = document.getElementById('menu');
const theme = document.getElementById('theme');
const side = document.getElementById('side');
const blurs = document.getElementById('blur');


function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

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

let themeanim = lottie.loadAnimation({
    container: theme,
    renderer: 'svg',   
    loop: false,     
    autoplay: false, 
    path: `${static}graphics/lottie/theme-f.json`
});

let themeanim2 = lottie.loadAnimation({
    container: theme,
    renderer: 'svg',   
    loop: false,     
    autoplay: false, 
    path: `${static}graphics/lottie/theme-b.json`
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

themeanim2.addEventListener('DOMLoaded', () => {
    let svgElement = themeanim.renderer.svgElement;
    let svgElement2 = themeanim2.renderer.svgElement;

    if (svgElement && svgElement2) {
        console.log('da');
        
        if (getCookie('theme') === 'light') {
            svgElement2.style.display = 'none';
        } else {
            svgElement.style.display = 'none';
        }
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

themeanim.addEventListener('complete', () => {
    isplayingtheme = false;
    themeanim2.renderer.svgElement.style.display = 'block';
    themeanim.renderer.svgElement.style.display = 'none';
    themeanim2.goToAndStop(0, true);
});

themeanim2.addEventListener('complete', () => {
    isplayingtheme = false;
    themeanim.renderer.svgElement.style.display = 'block';
    themeanim2.renderer.svgElement.style.display = 'none';
    themeanim.goToAndStop(0, true);
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
            openSide();
            menuanim.play()
        } else {
            menuanim2.play();
        }
    }
});

function openSide() {
    blurs.style.opacity = '1';
}

function closeSide() {
    
}

window.addEventListener('click', event => {
    console.log(event.target)
    if (!side.contains(event.target) && !event.target.matches('#side, #side *') && opened) {
        opened = false
        isplayingmenu = true
        menuanim2.play();
    }
});

let isplayingtheme = false;

function setTheme(theme) {
    if (theme == 'light') {
        document.documentElement.style.setProperty('--bg-col', 'white');
        document.documentElement.style.setProperty('--head-col', 'orange');
        document.documentElement.style.setProperty('--text-col', 'black');
        document.documentElement.style.setProperty('--el-col', 'white');
        document.documentElement.style.setProperty('--theme-col', 'white');
        document.documentElement.style.setProperty('--mix-percentage', '20%');
    } else {
        document.documentElement.style.setProperty('--bg-col', 'gray');
        document.documentElement.style.setProperty('--head-col', '#590059');
        document.documentElement.style.setProperty('--text-col', 'white');
        document.documentElement.style.setProperty('--el-col', 'white');
        document.documentElement.style.setProperty('--theme-col', 'black');
        document.documentElement.style.setProperty('--mix-percentage', '40%');
    }
}

theme.addEventListener('click', () => {
    if (!isplayingtheme) {
        isplayingtheme = true;
        if (getCookie('theme') == 'light') {
            document.cookie = 'theme=dark;';
            setTheme('dark');
            themeanim.play();
        } else {
            document.cookie = 'theme=light;';
            setTheme('light');
            themeanim2.play();
        }
    }
});
