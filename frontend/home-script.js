// Variables
const barsMenu = document.getElementById("bars-menu");
const menu = document.getElementById("menu");
const cardLeft = document.getElementById("card-left");
const cardRight = document.getElementById("card-right");
const combinedCard = document.getElementById("combined-cards");

const cardsLeft = ["images/RIGHT_1.png", "images/LEFT_1.png"];
const cardsRight = ["images/LEFT_1.png", "images/RIGHT_1.png"];
const combinedCards = ["images/LEFT_1.png", "images/RIGHT_1.png"];
let index_1 = 0;
let index_2 = 0;
let index = 0;

// Event Listeners
barsMenu.addEventListener("click", toggleMenu);

// Function to toggle menu
function toggleMenu() {
    barsMenu.classList.toggle("active");
    menu.classList.toggle("active");
}

// Function to change image
function changeImage(imageElement, imageArray, index, direction) {
    const translateX = direction === "left" ? "-100%" : "100%";
    imageElement.style.transform = `translateX(${translateX})`;
    setTimeout(() => {
        imageElement.src = imageArray[index];
        imageElement.style.transform = "translateX(0%)";
    }, 500);
}

// Functions to change cards
function changeCards() {
    changeImage(cardLeft, cardsLeft, index_1, "left");
    changeImage(cardRight, cardsRight, index_2, "right");
    index_1 = (index_1 + 1) % cardsLeft.length;
    index_2 = (index_2 + 1) % cardsRight.length;
}

function changeCardsCombineds() {
    changeImage(combinedCard, combinedCards, index, "left");
    index = (index + 1) % combinedCards.length;
}

// Set intervals for changing cards
setInterval(changeCards, 3000);
setInterval(changeCardsCombineds, 3000);

// Function to move the carousel
const productWidth = document.querySelector('.product-container').offsetWidth + 30;
let currentIndex = 0;
let container;

function moveCarousel(direction, containerIndex) {
    container = containerIndex === 0 ? document.querySelector('.carousel-0') : document.querySelector('.carousel-1');
    currentIndex += direction * 5;
    currentIndex = Math.min(Math.max(currentIndex, 0), 10);

    const translateX = -currentIndex * productWidth;
    container.style.transform = `translateX(${translateX}px)`;
}

// Event Listeners for carousel navigation
document.querySelector('.prev-button-0').addEventListener('click', () => moveCarousel(-1, 0));
document.querySelector('.next-button-0').addEventListener('click', () => moveCarousel(1, 0));
document.querySelector('.prev-button-1').addEventListener('click', () => moveCarousel(-1, 1));
document.querySelector('.next-button-1').addEventListener('click', () => moveCarousel(1, 1));