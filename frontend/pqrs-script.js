const containers = document.querySelectorAll('.container');
const buttons = document.querySelectorAll('.button');

function mostrarContenedor(index) {
  containers.forEach((container, i) => {
    container.classList.toggle("active", i === index);
  });
}

buttons.forEach((button, index) => {
  button.addEventListener('click', () => mostrarContenedor(index));
});