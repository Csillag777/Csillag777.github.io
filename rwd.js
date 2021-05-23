
  // When the user scrolls down 20px from the top of the document, slide down the navbar
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
  
