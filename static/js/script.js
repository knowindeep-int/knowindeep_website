// window.onclick = function(){
// }

document.addEventListener('DOMContentLoaded', function() {
    var element = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(element, options);
});

function mousein() {
    var a = document.getElementById("srch");
    a.classList.add("mystyle");
}


function myFunc() {
    document.getElementById("form").classList.add("form1");
    // var navs=document.getElementsByClassName('nav-item1');
    // navs[0].classList.add('hidden');
    // navs[1].classList.add('hidden');
}
function getLoginPopUp(){
    document.getElementsByTagName('body')[0].setAttribute('style', 'position: fixed;background-color: #d0d0d0;')
    document.getElementById('login_div').setAttribute('style', 'display: block;')
}
document.onclick = function(event) {

    if ( event.target.id != 'loginLink cate' && event.target.parentElement.className != "innner" &&  event.target.className != "outerr" && event.target.parentElement.className != "or_div" && event.target.parentElement.className != "outerr" && document.getElementById('login_div').style.display == 'block') {
        document.getElementById('login_div').style.display = "none";
        document.getElementsByTagName('body')[0].setAttribute('style', 'position: relative;background-color: #ffffff;')
    }


    if (!event.target.matches('#navbarDropdown')) {
        var dropdowns = document.getElementsByClassName("dropdown-menu");
        var myDropdown = document.getElementById("form");
        var z = document.getElementById("i");
        // var navs=document.getElementsByClassName('nav-item1');
        // if(navs[0].classList.contains('hidden')){
        //     navs[0].classList.remove('hidden')
        //     navs[1].classList.remove('hidden')
        // }
        if (myDropdown.classList.contains('form1')) {
            myDropdown.classList.remove('form1');
        }
        if (z.classList.contains('hidden')) {
            z.classList.remove('hidden');
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

function hide() {
    var c = document.getElementById("i");
    c.classList.add("hidden");
}


/* FOR BASE */ 

function implementSearch() {
    

    search_input = document.getElementById('search_input').value;
    $.ajax({
        url: '{% url "api:search" %}',
        method: "GET",
        data: {
            'search_input': search_input,
        },
        success: function(data) {
            var result = document.getElementById("srch");
            result.innerHTML = "";
            result.innerHTML += '<p class="list-group-item" style="color:black;" >Projects:</p>'
            for (var i = 0; i < data.projects.length; i++) {
                result.innerHTML += '<a class="list-group-item" href="/' + data.projects[i].slug + '" >' + data.projects[i].title + '</a>';
            }

            result.innerHTML += '<p class="list-group-item" style="color:black;" >Chapters:</p>'
            for (var i = 0; i < data.chapters.length; i++) {
                result.innerHTML += '<a class="list-group-item" href="/' + data.chapters[i].project_slug + '/' + data.chapters[i].slug + '" >' + data.chapters[i].heading + '</a>';
            }

            result.innerHTML += '<p class="list-group-item" style="color:black;" >Authors:</p>'
            for (var i = 0; i < data.authors.length; i++) {
                result.innerHTML += '<a class="list-group-item" href="/@' + data.authors[i].username + '" >' + data.authors[i].username + '</a>';
            }

        },
        error: function(error) {
            console.log('error')
        },
    });
};

function functionOne() {
    var x = document.getElementById("myLinks");
    if (x.style.display === "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
    }
}

window.addEventListener("resize", function() {
    var a = window.innerWidth;
    if (a > 993) {
        var x = document.getElementById("myLinks");
        x.style.display = "none";
    }
});

window.onscroll = function() {
    myFunction()
};

function myFunction() {
    var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    var scrolled = (winScroll / height) * 100;
    // document.getElementById("myBar").style.width = scrolled + "%";
}

// (function() { var dialog = document.getElementById('loginDialog'); document.getElementById('loginLink').onclick = function() { dialog.style.display = "block"; }; window.onclick = function() { if (event.target == dialog) { dialog.style.display = "none";
//         }; }; document.getElementById('googleLogin').onclick = function() { var url = this.getAttribute('google-href') window.open(url,"_self") }; document.getElementById('closeDialog').onclick = function() { dialog.style.display = "none"; }; document.getElementById('githubLogin').onclick
//         = function() { var url = this.getAttribute('github-href') window.open(url,"_self") }; // document.addEventListener('DOMContentLoaded', function() { // var element = document.querySelectorAll('.sidenav'); // var instances = M.Sidenav.init(element,
//         options);

        /* FOR DROPDOWN */ 
        // window.onclick = function(event) {
        //     if (!event.target.matches('.dropbtn') && !event.target.matches('.dropbtn img')) {     
        //       var dropdowns = document.getElementsByClassName("dropdown-content");
        //       var i;
        //       for (i = 0; i < dropdowns.length; i++) {
        //         var openDropdown = dropdowns[i];
        //         if (openDropdown.classList.contains('show')) {
        //           openDropdown.classList.remove('show');
        //         }
        //       }
              
        //     }
        
        //   }

        //   let test = document.getElementById("navbarDropdown");

        //   test.addEventListener("mouseover", function( event ) {
        //       var a = document.getElementById("srch");
        //       a.classList.toggle("mystyle");
          
        //   }, false);
          
function mouseOut() {	var a = document.getElementById("srch");
a.classList.remove("mystyle");
}
function mousein() {	var a = document.getElementById("srch");
a.classList.add("mystyle");
}   
function hide(){
    var c=document.getElementById("i");
    c.classList.add("hidden");
}

