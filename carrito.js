// cart.js

// Función para incrementar la cantidad
function incrementValue() {
    const quantityElement = document.getElementById("quantity");
    quantityElement.stepUp();
}

// Función para decrementar la cantidad
function decrementValue() {
    const quantityElement = document.getElementById("quantity");
    quantityElement.stepDown();
}
document.addEventListener("DOMContentLoaded", function () {
  const menuIcon = document.querySelector(".menu-icon");
  const mobileMenu = document.querySelector(".mobile-menu");

  menuIcon.addEventListener("click", function () {
    if (mobileMenu.style.display === "block") {
      mobileMenu.style.display = "none";
    } else {
      mobileMenu.style.display = "block";
    }
  });
});




