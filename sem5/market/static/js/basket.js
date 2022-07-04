let basketCount = document.getElementById("basket-count");
let items = document.getElementsByClassName("item");

Array.from(items).forEach((element) => {
    let buyButton = element.querySelector(".buy-button");
    let itemId = element.querySelector(".item-id").value;
    buyButton.onclick = function() {
        console.log(itemId)
        $.ajax({
            url: '/market/',
            dataType: 'json',
            type: 'post',
            contentType: 'application/json',
            data: JSON.stringify({
                "item-id": itemId
            }),
            success: function(data, textStatus, jQxhr) {
                console.log("success");
                console.log(data);
                basketCount.innerHTML = data;
            },
            error: function(jqXhr, textStatus, errorThrown) {
                console.log("failed");
            }
        });
    };
});
