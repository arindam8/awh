function toggle_form() {
    var pop_up = document.getElementById("popup_jumbo");
    if (pop_up.style.visibility == "hidden") {
        pop_up.style.visibility = "visible";
        fadeOut()
    } else {
        pop_up.style.visibility = "hidden";
        fadein()
    }
}

function fadeOut() {
    var fadeTarget = document.getElementById("enquire_widget");
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
    }, 50);
}

function fadein() {
    var fadeTarget = document.getElementById("enquire_widget");
    fadeTarget.classList.remove('playstate');
    fadeTarget.style.opacity = 1
}