switcharoony();

window.addEventListener("resize", switcharoony);

function switcharoony() {
    var tabs_large = document.getElementsByClassName("tabs_large");
    var tabs_small = document.getElementsByClassName("tabs_small");
    var i;

    var w = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
    var h = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);

    if (w <= 768) {
        for (i = 0; i < tabs_large.length; i++) {
            j = i+1;
            var dynamic_name = "collapse" + j;
            tabs_small[i].setAttribute("id", dynamic_name);
            tabs_large[i].removeAttribute("id");
        }
    }

    if (w > 768) {
        for (i = 0; i < tabs_large.length; i++) {
            j = i+1;
            var dynamic_name = "collapse" + j;
            tabs_large[i].setAttribute("id", dynamic_name);
            tabs_small[i].removeAttribute("id");
        }
    }
}