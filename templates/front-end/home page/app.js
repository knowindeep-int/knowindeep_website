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
    if(window.innerWidth<1220){
    var qw=document.querySelectorAll(".nav-item");
    qw[0].classList.add("hidden");
    qw[1].classList.add("hidden");
    }
}

window.onclick = function(event) {
  if (!event.target.matches('#navbarDropdown')) {
    var dropdowns = document.getElementsByClassName("dropdown-menu");
    var myDropdown = document.getElementById("form");
    var qw=document.querySelectorAll(".nav-item");
    if (myDropdown.classList.contains('form1')) {
      myDropdown.classList.remove('form1');
      qw[0].classList.remove("hidden");
      qw[1].classList.remove("hidden");
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

