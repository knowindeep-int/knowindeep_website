// function myfunction(){
// 	var x=document.getElementById("navbarDropdown")
	
// }

// function functionOne() {
//      var x = document.getElementById("myLinks");
//      if (x.style.display === "block") {
//          x.style.display = "none";
//      } else {
//          x.style.display = "block";
//      }
//  }

//   window.addEventListener("resize", function() {
//       var a = window.innerWidth;
//       if (a > 993) {
//           var x = document.getElementById("myLinks");
//           x.style.display = "none";
//       }
// });


function mousein() {	var a = document.getElementById("srch");
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

