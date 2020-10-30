$(window).scroll(function(){
    var h = window.innerHeight;
    $('nav').toggleClass('scrolled', $(this).scrollTop() > (h*0.8));
});

