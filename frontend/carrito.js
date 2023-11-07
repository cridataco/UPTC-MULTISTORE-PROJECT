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


document.addEventListener('DOMContentLoaded', function() {
    // Obten el botón de ePayco y el menú emergente
    var epaycoButton = document.getElementById('epayco-button');
    var epaycoPopup = document.getElementById('epayco-popup');
    var epaycoOverlay = document.getElementById('epayco-overlay');

    // Agrega un manejador de eventos al botón de ePayco
    epaycoButton.addEventListener('click', function() {
        epaycoButton.style.display = 'block';
        epaycoPopup.style.display = 'block';
        epaycoOverlay.style.display = 'block';
    });

    epaycoOverlay.addEventListener('click', function() {
        epaycoPopup.style.display = 'none';
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

    // Agregar un manejador de eventos al botón de enviar notificación
    sendNotificationButton.addEventListener('click', function() {
        var message = 'Apreciado Usuario, continue el proceso de pago de su producto de nuestra tienda MultiStore UPTC';

    // Realizar una solicitud a la API de Nequi para enviar una notificación
    fetch('https://api.nequi.com/notification', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Basic ' + btoa(clientId + ':' + clientSecret) // Autenticación básica
        },
        body: JSON.stringify({
            phone: phoneNumber,
            message: message
        })
    })
    .then(function(response) {
        if (response.ok) {
            // La notificación se envió con éxito
            console.log('Notificación enviada con éxito');
        } else {
            // Hubo un error al enviar la notificación
            console.error('Error al enviar la notificación');
        }
    })
    .catch(function(error) {
        console.error('Error de red:', error);
    });
      

        // Ocultar el formulario después de enviar la notificación
        nequiPopup.style.display = 'none';
    });

    nequiOverlay.addEventListener('click', function() {
        nequiPopup.style.display = 'none';
        nequiOverlay.style.display = 'none';
    });
});




fetch('https://checkout.epayco.co/checkout.js', {
    method: "POST",
    body: JSON.stringify({
        key: "4bf5a941ed420c376a7fb0d45766244a",
        name: "Vestido Mujer Primavera",
        description: "Vestido Mujer Primavera",
        currency: "cop",
        amount: 50000,
        tax: 15000,
        country: "co",
        lang: "es",
        test: true
    }),
    headers: { "Content-type": "application/json; charset=UTF-8" }
})
    .then(response => response.json())
    .then(({ data: { sessionId } }) => {
        const handler = ePayco.checkout.configure({
            sessionId,
            external: false // external: true -> para checkout externo ó External: false => para iframe onePage
        })
        //open checkout
        handler.openNew()
    })
    .catch(error => console.log(error))

