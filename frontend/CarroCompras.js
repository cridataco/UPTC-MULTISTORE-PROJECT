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

function pagarEpayco(){
  var handler = ePayco.checkout.configure({
      key: "4bf5a941ed420c376a7fb0d45766244a",
      test: true
  })

  var data = {

      name: "Vestido Mujer Primavera",
      description: "Vestido Mujer Primavera",
      invoice: "",
      currency: "cop",
      amount: "50000",
      tax_base: "0",
      tax: "0",
      country: "CO",
      lang: "es",
      external:false
  }

  handler.open(data);
}

  document.addEventListener('DOMContentLoaded', function() {
      // Obten el botón de ePayco y el menú emergente
      var epaycoButton = document.getElementById('epayco-button');
      var epaycoOverlay = document.getElementById('epayco-overlay');
  
      // Agrega un manejador de eventos al botón de ePayco
      epaycoButton.addEventListener('click', function() {
          epaycoButton.style.display = 'block';
          pagarEpayco();
          epaycoOverlay.style.display = 'block';
          
      });
  
      epaycoOverlay.addEventListener('click', function() {
          epaycoOverlay.style.display = 'none';
      });
  });



document.addEventListener('DOMContentLoaded', function() {
  // Obtener el botón de Nequi y el formulario de Nequi
  var nequiButton = document.getElementById('nequi-button');
  var nequiPopup = document.getElementById('nequi-popup');
  var nequiOverlay = document.getElementById('nequi-overlay');
  var sendNotificationButton = document.getElementById('send-notification-button');
  var clientId = '1p4pc5lif1u9kte3jgfijgfpk2';
  var clientSecret = '2dhpaaddlqja61n3nop5mdai7hfmhtauddt09b2uakqccrqi4ab';

  // Agregar un manejador de eventos al botón de Nequi
  nequiButton.addEventListener('click', function() {
      // Mostrar el formulario de Nequi al hacer clic en el botón
      nequiPopup.style.display = 'block';
      nequiOverlay.style.display = 'block';
  });

  
  nequiOverlay.addEventListener('click', function() {
      nequiPopup.style.display = 'none';
      nequiOverlay.style.display = 'none';
  });
});






