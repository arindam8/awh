document.addEventListener('DOMContentLoaded', function() {
    /********************
    change the text in the attach label
    ********************/
    default_attach = document.getElementById('id_attach');
    default_attach.onchange = function() {
        const fileName = default_attach.value;
        document.getElementById("file-selected").textContent=fileName.replace(/^.*\\/, "");
    };

    /********************
    style the bullet points dynamicly
    ********************/
    const points = document.querySelectorAll('.more_info');
    points.forEach((point, index) => {
        const delay = index * 200;
        point.style.transitionDelay = `${delay}ms`;
        const top = 50 + (index * 10);
        point.style.top =  `calc(${top}% + 85px)`
    });

    var w = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
    var h = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);


    /********************
    intersection funcs
    ********************/
    function enq(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                document.querySelector('#enquire_widget').classList.add('enquire_widget_vis');
                document.querySelector('#enquire_widget_mini').classList.add('enquire_widget_vis');
                document.querySelector('#phone_widget_mini').classList.add('enquire_widget_vis');
            } else {
                document.querySelector('#enquire_widget').classList.remove('enquire_widget_vis');
                document.querySelector('#enquire_widget_mini').classList.remove('enquire_widget_vis');
                document.querySelector('#phone_widget_mini').classList.remove('enquire_widget_vis');
            }
        });
    };

    function boxs(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                Array.from(entry.target.children).forEach((child) => {
                    if (child.classList.contains("facts")) {
                        child.classList.add('no_hover');
                    }
                    if (child.classList.contains("more_info")) {
                        child.classList.add('no_hover_info');
                    }
                    if (child.classList.contains("about_btn")) {
                        child.classList.add('about_btn_no_hov');
                    }
                    if (child.classList.contains("tel_num")) {
                        document.querySelector('.large_phone').classList.add('large_phone_no_hov');
                    }
                })
            }
            else {
                Array.from(entry.target.children).forEach((child) => {
                    if (child.classList.contains("facts")) {
                        child.classList.remove('no_hover');
                    }
                    if (child.classList.contains("more_info")) {
                        child.classList.remove('no_hover_info');
                    }
                    if (child.classList.contains("about_btn")) {
                        child.classList.remove('about_btn_no_hov');
                    }
                    if (child.classList.contains("tel_num")) {
                        document.querySelector('.large_phone').classList.remove('large_phone_no_hov');
                    }
                })
            }
        })
    }

    /********************
    observe enquiery form
    ********************/
    var observer = new IntersectionObserver(enq);
    var target = document.querySelector('#enquire_jumo');
    observer.observe(target);

    if (w <= 768) {
        /********************
        observe box's on only on small screens
        ********************/
        var options = {
          rootMargin: '-50%',
          threshold: 0
        }
        var observer1 = new IntersectionObserver(boxs, options);
        document.querySelectorAll('.boxs').forEach(box => observer1.observe(box));
    }
}, false);

window.addEventListener('load', function() {
    /********************
    stop enquire buttons flashing up
    ********************/
    document.querySelector('#enquire_widget').style.visibility = "visible";
    document.querySelector('#enquire_widget_mini').style.visibility = "visible";
    document.querySelector('#phone_widget_mini').style.visibility = "visible";
});