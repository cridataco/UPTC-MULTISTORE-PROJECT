document.addEventListener("DOMContentLoaded", function () {
    const largeImage = document.getElementById("largeImage");
    const thumbnails = document.querySelectorAll(".thumbnails img");
    const comentarioImages = document.querySelectorAll(".comentario-image");

    thumbnails.forEach(thumbnail => {
        thumbnail.addEventListener("click", () => {
            largeImage.src = thumbnail.src;
            largeImage.classList.add("zoomed"); // Agrega una clase para la expansión
        });
    });

    largeImage.addEventListener("click", () => {
        largeImage.classList.remove("zoomed"); // Elimina la clase para volver al tamaño original
    });

   
    
        comentarioImages.forEach(image => {
            image.addEventListener("click", () => {
                image.classList.toggle("expanded");
            });
        });
    
    
        const productImage = document.querySelector(".product-image img");
        const colourButtons = document.querySelectorAll(".btn-colour");
    
        // Función para cambiar la imagen principal
        function changeMainImage(imageSrc) {
            productImage.src = imageSrc;
        }
    
        // Asocia un evento de clic a cada botón de color
        colourButtons.forEach(button => {
            button.addEventListener("click", () => {
                const imageSrc = button.getAttribute("data-image");
                changeMainImage(imageSrc);
            });
        });
    
        thumbnails.forEach(thumbnail => {
            thumbnail.addEventListener("click", () => {
                productImage.src = thumbnail.src;
            });
        });

    const estrellasVotables = document.querySelectorAll('.estrellas .estrella');
    const estrellasReflejadas = document.querySelectorAll('.estrellas-solo-lectura .estrella');
    const promedioElement = document.getElementById('promedio');
    const promedioElement2 = document.getElementById('promedio2');
    const votosElement = document.getElementById('votos');

    let calificacionActual = parseFloat(promedioElement.textContent);
    
    let calificacionActual2 = parseFloat(promedioElement2.textContent);
    let votos = parseInt(votosElement.textContent);

    estrellasVotables.forEach(estrella => {
        estrella.addEventListener('click', () => {
            const valor = parseInt(estrella.getAttribute('data-valor'));
            calificacionActual = (calificacionActual * votos + valor) / (votos + 1);
            calificacionActual2 = (calificacionActual * votos + valor) / (votos + 1);
            votos++;

            promedioElement.textContent = calificacionActual.toFixed(1);
            promedioElement2.textContent = calificacionActual2.toFixed(1);
            votosElement.textContent = votos;

            // Actualizar las estrellas reflejadas (las pequeñas)
            estrellasReflejadas.forEach((estrella, index) => {
                if (index < valor) {
                    estrella.innerHTML = '★';
                } else {
                    estrella.innerHTML = '☆';
                }
            });
        });
    });
});
