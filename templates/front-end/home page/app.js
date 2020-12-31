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
let test = document.getElementById("navbarDropdown");

test.addEventListener("mouseover", function( event ) {
	var a = document.getElementById("srch");
    a.classList.toggle("mystyle");

}, false);

function mouseOut() {	var a = document.getElementById("srch");
a.classList.remove("mystyle");
}