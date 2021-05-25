
   /* When the user scrolls down 20px from the top of the document, slide down the navbar
  window.onscroll = function () { scrollFunction() };

  function scrollFunction() {
    if (document.body.scrollTop > 156 || document.documentElement.scrollTop > 156) {
      //document.getElementById("n2").style.top = "0px";
      document.getElementById("n1").style.position = "relative";
      document.getElementById("n1").style.top = "0px";
    } else {
      //document.getElementById("n2").style.top = -"-100px";
      document.getElementById("n1").style.position = "relative";
    }
  }
  
*/
function menu{
  document.getElementById("c2").style.display = block;
}

/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
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
