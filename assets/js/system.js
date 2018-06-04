window.onscroll = function () {
    do_scroll()
  };

function do_scroll() {
    var nav = document.getElementById('nav')
    if (document.documentElement.scrollTop >= 72 || document.body.scrollTop >= 72) {
        nav.style.position = 'fixed';
        nav.style.top = '0';
    } else {
        nav.style.position = 'absolute';
        nav.style.top = '';
    }
  }