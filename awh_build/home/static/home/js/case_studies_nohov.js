document.addEventListener('DOMContentLoaded', function() {

    var w = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
    var h = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);


    function case_zoomer(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('case_box_ho_hov');
            }
            else {
                entry.target.classList.remove('case_box_ho_hov');
            }
        })
    }


    if (w <= 768) {
        //observe box's on small screen
        var options = {
          rootMargin: '-50%',
          threshold: 0
        }
        var observer2 = new IntersectionObserver(case_zoomer, options);
        document.querySelectorAll('.case_img').forEach(box => observer2.observe(box));
    }
});