const priceMin = document.getElementById("price_min");
const priceMax = document.getElementById("price_max");
const minPriceValue = document.getElementById("min-price-value");
const maxPriceValue = document.getElementById("max-price-value");

// Оновлення повзунків
function updateSlider() {
    let min = parseInt(priceMin.value);
    let max = parseInt(priceMax.value);

    // Уникаємо перетину повзунків
    if (min >= max) {
        priceMin.value = max - 50;
        min = max - 50;
    }

    if (max <= min) {
        priceMax.value = min + 50;
        max = min + 50;
    }

    // Оновлення значень на екрані
    minPriceValue.textContent = priceMin.value;
    maxPriceValue.textContent = priceMax.value;
}

// Додати обробники подій для кожного повзунка
priceMin.addEventListener("input", updateSlider);
priceMax.addEventListener("input", updateSlider);

// Початкове оновлення
updateSlider();