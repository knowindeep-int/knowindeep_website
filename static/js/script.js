document.addEventListener('DOMContentLoaded', function() {
    var element = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(element, options);
});

// function myfunc() {
//  {% if request.user.is_authenticated %}
//         window.open("{% url 'site_users:logout' %}", "", "width=700,height=700");
//     {% else %}
//         window.open("{% url 'social:begin' 'google-oauth2' %}?next={{request.path}}", "", "width=700,height=700");
//     {% endif %}
// }


/* FOR BASE */ 

function implementSearch() {
    
    alert('fuck js');
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
            alert(error)
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

(function() { var dialog = document.getElementById('loginDialog'); document.getElementById('loginLink').onclick = function() { dialog.style.display = "block"; }; window.onclick = function() { if (event.target == dialog) { dialog.style.display = "none";
        }; }; document.getElementById('googleLogin').onclick = function() { var url = this.getAttribute('google-href') window.open(url,"_self") }; document.getElementById('closeDialog').onclick = function() { dialog.style.display = "none"; }; document.getElementById('githubLogin').onclick
        = function() { var url = this.getAttribute('github-href') window.open(url,"_self") }; // document.addEventListener('DOMContentLoaded', function() { // var element = document.querySelectorAll('.sidenav'); // var instances = M.Sidenav.init(element,
        options);

        /* FOR DROPDOWN */ 
        window.onclick = function(event) {
            if (!event.target.matches('.dropbtn') && !event.target.matches('.dropbtn img')) {     
              var dropdowns = document.getElementsByClassName("dropdown-content");
              var i;
              for (i = 0; i < dropdowns.length; i++) {
                var openDropdown = dropdowns[i];
                if (openDropdown.classList.contains('show')) {
                  openDropdown.classList.remove('show');
                }
              }
              
            }
        
          }

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