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


    let allpizzaex = document.createElement("button")
    let header = document.createElement("h2");
    header.textContent = "CART"
    allpizzaex.className = "pizzaex"
    allpizzaex.onclick = () => deletecart();

    cart_list.appendChild(allpizzaex);
    cart_list.appendChild(header);
    
    // all pizza boxes
    for (let i = 0; i < cart.length; i++) {
        // PIZZAS
        let pizzaItem = document.createElement("li");

        let pizzaName = document.createElement("h4");
        let pizzaImg = document.createElement("img");
        let pizzaPrice = document.createElement("h5")
        let pizzaex = document.createElement("button")
        let pizzaquant = document.createElement("input")

        pizzaItem.id = "pizzaitem"
        pizzaName.textContent = cart[i].name;

        pizzaImg.src = "/static/" + cart[i].image;
        pizzaImg.id = "cart_img"

        pizzaPrice.textContent = cart[i].price + "kr"

        pizzaex.className = "pizzaex"
        pizzaex.onclick = () => deletepizza(cart[i].id);

        pizzaquant.type = "number"
        pizzaquant.value = 1
        pizzaquant.style = "width: 50px; margin-right: 200px;"


        pizzaItem.appendChild(pizzaName);
        
        pizzaItem.appendChild(pizzaPrice);
        pizzaItem.appendChild(pizzaImg);
        
        pizzaItem.appendChild(pizzaquant);
        pizzaItem.appendChild(pizzaex);

        cart_list.appendChild(pizzaItem);

        price += cart[i].price
    }

    let footer_price = document.createElement("h3");
    footer_price.textContent = "Total: " + price + "kr"

    cart_list.appendChild(footer_price);
    
    let checkout_btn = document.createElement("a");
    checkout_btn.textContent = "Checkout"
    checkout_btn.style = "width: 100px; background-color: orange;"
    checkout_btn.href = "{% url 'home-cart' %}";
    
    cart_list.appendChild(checkout_btn);
}


const deletepizza = (id) => {
    console.log("delete ein pizza")
    cart.forEach(el => {
        if (el == id) {
            cart.splice(el)
        }
    });
}

const deletecart = () => {
    cart = []
    displayCart()
    console.log("delete cart")
}