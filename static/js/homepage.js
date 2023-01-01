var i = 0;
function move() {
  if (i == 0) {
    i = 1;
    var elem = document.getElementById("myBar");
    var width = 0;
    var id = setInterval(frame, 65);
    function frame() {
      if (width >= 100) {
        clearInterval(id);
        i = 0;
        window.location.href = "/homePage";
      } else {
        width++;
        elem.style.width = width + "%";
        elem.innerHTML = "Fetching Details";
      }
    }
  }
}