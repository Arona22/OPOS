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

    let header = document.createElement("h2");
    
    for (let i = 0; i < cart.length; i++) {
        // PIZZAS
        let pizzaItem = document.createElement("li");
        let pizzaName = document.createElement("h4");
        let pizzaImg = document.createElement("img");

        pizzaItem.id = "pizzaitem"
        pizzaName.textContent = cart[i].name;

        pizzaImg.src = "/static/" + cart[i].image;
        pizzaImg.id = "cart_img"

        pizzaItem.appendChild(pizzaName);
        pizzaItem.appendChild(pizzaImg);

        cart_list.appendChild(pizzaItem);
    }
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
