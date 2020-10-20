<<<<<<< HEAD
var checklist = document.getElementsByClassName("checklist");
=======
/*var checklist = document.getElementsByClassName("checklist");
>>>>>>> 13b1dda (test)
var items = document.querySelectorAll("li");
var inputs = document.querySelectorAll("input");
for (var i = 0;i<items.length;i++){
    items[i].addEventListener("click" , write);
    inputs[i].addEventListener("blur" , update);
}
function write(){
    this.className = "edit";
    var input = this.querySelector("input");
    input.focus();
    input.setSelectionRange(0,input.value.length);
}
function update(){
    this.previousElementSibling.innerHTML = this.value;
    this.parentNode.className = "";
<<<<<<< HEAD
}
document.getElementById("11").onclick = function() {alert("goodjob")};
function flask_open(){
    window.location.href = "f.html";
}
function w(){
    window.location.href = "f.html";
}
=======
}*/
//document.getElementById("11").onclick = function() {alert("goodjob")};
var i = "intro.html";
function homeredirect(){
    window.location.href = "index.html";
}
function pageredirect(){
    window.location.href = i;
}
function introredirect(){
    window.location.href = "intro.html";
}
function eduredirect(){
    window.location.href = "edu.html";
}

function proredirect(){
    window.location.href = "pro.html";
}

function conredirect(){
    window.location.href = "contact.html";
}

function supredirect(){
    window.location.href = "sup.html";
}

function resredirect(){
    window.location.href = "res.html";
}
function apologize(){
    alert("Sorry, This language is still preparing. TAT");
}
>>>>>>> 13b1dda (test)
