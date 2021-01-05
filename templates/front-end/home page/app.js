// this is for the change in the navbar on scroll

// $(window).scroll(function () {
//     var scroll = $(window).scrollTop();
//     var box = $('.header-text').height();
//     var header = $('header').height();

//     if (scroll >= box - header) {
//         $("header").addClass("background-header");
//     } else {
//         $("header").removeClass("background-header");
//     }
// });

function mousein() {	
    var a = document.getElementById("srch");
    a.classList.add("mystyle");
}

function myFunc(){
    document.getElementById("form").classList.add("form1");
}

window.onclick = function(event) {
  if (!event.target.matches('#navbarDropdown')) {
    var dropdowns = document.getElementsByClassName("dropdown-menu");
    var myDropdown = document.getElementById("form");
    if (myDropdown.classList.contains('form1')) {
      myDropdown.classList.remove('form1');
    }
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('mystyle')) {
        openDropdown.classList.remove('mystyle');
      }
    }
  }
}

