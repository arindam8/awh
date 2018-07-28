var pop_up = document.getElementById("popup_jumbo");
var pop_up_slide = document.getElementsByClassName("pop_up_transition")[0];
var fadeTarget = document.getElementById("enquire_widget");

function toggle_form() {
    if (pop_up.style.visibility == "hidden") {
        fadeOut()
        slideIn()
    } else {
        slideOut()
        fadein()
    }
}

function fadeOut() {
    fadeTarget.classList.add('playstate');
    var fadeEffect = setInterval(function () {
        if (!fadeTarget.style.opacity) {
            fadeTarget.style.opacity = 1;
        }
        if (fadeTarget.style.opacity > 0) {
            fadeTarget.style.opacity -= 0.1;
        } else {
            clearInterval(fadeEffect);
        }
    }, 100);
}


function slideIn() {
    pop_up.style.visibility = "visible";
    pop_up_slide.classList.add("popup_jumbo_translate");
}

function slideOut() {
    pop_up_slide.classList.remove("popup_jumbo_translate");
    pop_up.style.visibility = "hidden";
}

function fadein() {
    fadeTarget.classList.remove('playstate');
    fadeTarget.style.opacity = 1
}