let categoriesMenuVisible = false;

function showCategoriesMenu() {
    const categoriesMenu = document.querySelector('.categories-menu');
    categoriesMenu.classList.add('fixed-menu');
    categoriesMenuVisible = true;
}

function hideCategoriesMenu() {
    if (!categoriesMenuVisible) {
        const categoriesMenu = document.querySelector('.categories-menu');
        categoriesMenu.classList.remove('fixed-menu');
    }
}

document.addEventListener('click', function (event) {
    const categoriesButton = document.querySelector('.categories-dropdown');
    const categoriesMenu = document.querySelector('.categories-menu');

    if (!categoriesButton.contains(event.target) && !categoriesMenu.contains(event.target)) {
        hideCategoriesMenu();
        categoriesMenuVisible = false;
    }
    
});


