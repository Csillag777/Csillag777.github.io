var checklist = document.getElementsByClassName("checklist");
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
}