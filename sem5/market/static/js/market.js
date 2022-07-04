var slider = document.getElementById("priceRange");
var priceValue = document.getElementById("priceValue");
priceValue.innerHTML = slider.value;

slider.oninput = function() {
    priceValue.innerHTML = this.value;
}
