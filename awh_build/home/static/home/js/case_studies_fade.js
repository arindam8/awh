var cube = document.getElementsByClassName("case_box");
var i;
var j;
var k = 9;

function toggle_fade(j) {
    j = j - 1;
    if (j == k) {
        all_off();
        k = 9;
    } else {
        one_on(j);
        k = j;
    }
}

function all_off() {
    for (i = 0; i < cube.length; i++) {
        cube[i].classList.remove("case_fade");
        cube[i].children[0].children[1].classList.remove("case_red");
    }
}

function one_on(j) {
    for (i = 0; i < cube.length; i++) {
        if (j != i) {
            cube[i].classList.add("case_fade");
            cube[i].children[0].children[1].classList.remove("case_red");
        } else {
            cube[i].classList.remove("case_fade");
            cube[i].children[0].children[1].classList.add("case_red");
        }
    }
}