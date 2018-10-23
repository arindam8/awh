//tabs
window.onload = function () {
    var index='{{index|escapejs}}';
    console.log(index);
    if (index==='-99'){
        var tab = document.getElementById("nav-menu0-tab");
        tab.classList.add("active");
        tab.classList.add("show");
        var info = document.getElementById("nav-menu0");
        info.classList.add("active");
        info.classList.add("show");
    }
    else{
        var elementId = "nav-menu" + index+"-tab";
        var tab = document.getElementById(elementId);
        console.log(elementId);
        tab.classList.add("active");
        tab.classList.add("show");
        var elid = "nav-menu" + index;
        var info = document.getElementById(elid);
        info.classList.add("active");
        info.classList.add("show");
    }
    if (index!='0' && index!='-99'){
        var tab = document.getElementById("nav-menu0-tab");
        tab.classList.remove("active");
        tab.classList.remove("show");
        var info = document.getElementById("nav-menu0");
        info.classList.remove("active");
        info.classList.remove("show");
    }

    for (i = 0; i++; i <= 6) {
        if (i != index) {
            var elementId = "nav-menu" + index+"-tab";
            tab = document.getElementById(elementId);
            tab.classList.remove("active")
            tab.classList.remove("show");
            var elid = "nav-menu" + index;
            var info = document.getElementById(elid);
            info.classList.remove("active");
            info.classList.remove("show");
        }
    }
};

//case studies
window.onload = function () {
    var index='{{index|escapejs}}';

    var elementId = "#collapse" + index;
        var elid="collapse" + index;
        console.log(elementId);
        qstring="a[href='"+elementId+"']";
        console.log(qstring);
        var tab=document.querySelectorAll(qstring);
        var info=document.getElementById(elid);
        console.log(tab);
        tab[0].classList.remove("collapsed");
        tab[0].setAttribute("aria-expanded", "true");
        info.classList.add("show");
};
