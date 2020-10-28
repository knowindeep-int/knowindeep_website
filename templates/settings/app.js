var p1 = document.getElementsByClassName("btn-group")
var p3 = document.getElementsByClassName("cancel")
var p2 = document.getElementsByClassName("edit")
var ele = 0;

function myFunction() {

	var i = 0;
	for (i = 0; i < p2.length - 1; i++) {
		p2[i].addEventListener("click", function () {
			p1[ele].classList.toggle("second");
			p2[ele].classList.toggle("second");
		});
		p3[i].addEventListener("click", function () {
			p1[ele].classList.toggle("second");
			p2[ele].classList.toggle("second");
		});
	}
}

myFunction();