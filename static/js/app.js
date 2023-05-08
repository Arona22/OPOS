const filtering = () => {
    const checkbox = document.getElementById("flexCheckDefault")
}

let cart = [
    {
        "id": 0,
        "name": "Margarita",
        "image": "img/marga_pizza.jpg",
        "price": 1199,
    },
    {
        "id": 1,
        "name": "OPOS Special",
        "image": "img/opos_pizza.jpg",
        "price": 1199,
    },
]

const add_cart = (pizza) => {
    cart.push(pizza)
}


const displayCart = () => {
    let cart_list = document.getElementById("cart_list");
    cart_list.innerHTML='';
    let price = 0

    let header = document.createElement("h2");
    header.textContent = "CART"

    cart_list.appendChild(header);
    
    for (let i = 0; i < cart.length; i++) {
        // PIZZAS
        let pizzaItem = document.createElement("li");

        let pizzaName = document.createElement("h4");
        let pizzaImg = document.createElement("img");
        let pizzaPrice = document.createElement("h5")
        let pizzaex = document.createElement("button")

        pizzaItem.id = "pizzaitem"
        pizzaName.textContent = cart[i].name;

        pizzaImg.src = "/static/" + cart[i].image;
        pizzaImg.id = "cart_img"

        pizzaPrice.textContent = cart[i].price + "kr"

        pizzaex.id = "pizzaex"

        pizzaItem.appendChild(pizzaName);
        pizzaItem.appendChild(pizzaPrice);
        pizzaItem.appendChild(pizzaImg);
        pizzaItem.appendChild(pizzaex);

        cart_list.appendChild(pizzaItem);

        price += cart[i].price
    }

    let footer_price = document.createElement("h3");
    footer_price.textContent = "Total: " + price + "kr"

    cart_list.appendChild(footer_price);

}


    let eatHeader = document.createElement("h3");
    let eatText = document.createTextNode("Name: " + response.data[i].name + "\n");
    eatItem.appendChild(eatHeader);
    eatItem.appendChild(eatText);
    eatList.appendChild(eatItem);

    const eatButton = document.createElement("button");
    eatButton.textContent = 'Show information'
    eatButton.onclick = () => displayInfo(response.data[i]);

    eatItem.appendChild(eatButton);

    eatList.appendChild(eatItem);
