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

// var p1 = document.getElementsByClassName("btn-group")
// var p3 = document.getElementsByClassName("cancel")
// var p2 = document.getElementsByClassName("edit")
// var ele = 0;

// function myFunction() {
// 	var i = 0;
// 	for (i = 0; i < p2.length - 1; i++) {
// 		p2[i].addEventListener("click", function () {
// 			p1[ele].classList.toggle("second");
// 			p2[ele].classList.toggle("second");
// 		});
// 		p3[i].addEventListener("click", function () {
// 			p1[ele].classList.toggle("second");
// 			p2[ele].classList.toggle("second");
//     });
//     ele++;
// 	}
// }

// myFunction();

function reply_click(e) {
  e.target.classList.toggle("second");
  var a=e.target.id;
  var p1 = document.getElementsByClassName("btn-group");
  var b= a-1;
  p1[b].classList.toggle("second");
}

function reply(e) {
  var txt = e.target.id;
  var numb = txt.match(/\d/g);
  var p1 = document.getElementsByClassName("btn-group");
  p1[numb-1].classList.toggle("second");
  var b=String(numb-1);
  p3=document.getElementById("b");
  p3.classList.toggle("second");
}