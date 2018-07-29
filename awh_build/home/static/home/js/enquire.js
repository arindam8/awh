var pop_up = document.getElementById("popup_jumbo");
var fadeTarget = document.getElementById("enquire_widget");
var toggle = 1;

function toggle_form() {
    if (toggle == 1) {
        toggle = 0;
        fadeOut()
        slideIn()
    } else {
        toggle = 1;
        slideOut()
        fadein()
    }
}

function fadeOut() {
    fadeTarget.classList.add('playstate');
    fadeTarget.classList.add('enquire_widget_translate');
}


function slideIn() {
    pop_up.classList.add("popup_jumbo_translate");
}

function slideOut() {
    pop_up.classList.remove("popup_jumbo_translate");
}

function fadein() {
    fadeTarget.classList.remove('playstate');
    fadeTarget.classList.remove('enquire_widget_translate');
}