const filtering = () => {
    const checkbox = document.getElementById("flexCheckDefault")
}

let cart = [
    {
        "id": 0,
        "name": "Margarita",
        "image": "img/marga_pizza.jpg",
        "price": 1199,
        "quantity": 1,
    },
    {
        "id": 1,
        "name": "OPOS Special",
        "image": "img/opos_pizza.jpg",
        "price": 1199,
        "quantity": 2,
    },
]

const add_cart = (pizza) => {
    if (cart.includes(pizza)) {
        cart
    }
    cart.push(pizza)
}



const displayCart = () => {
    let cart_list = document.getElementById("cart_list");
    cart_list.innerHTML='';
    let total = 0


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

        
        pizzaex.className = "pizzaex"
        pizzaex.onclick = () => deletepizza(cart[i].id);
        
        pizzaquant.value = cart[i].quantity
        pizzaquant.type = "number"
        pizzaquant.style = "width: 50px; margin-right: 200px;"
        
        pizzaPrice.textContent = cart[i].price + "kr"

        pizzaItem.appendChild(pizzaName);
        
        pizzaItem.appendChild(pizzaPrice);
        pizzaItem.appendChild(pizzaImg);
        
        pizzaItem.appendChild(pizzaquant);
        pizzaItem.appendChild(pizzaex);

        cart_list.appendChild(pizzaItem);

        total += cart[i].price * cart[i].quantity
    }

    let footer_price = document.createElement("h3");
    footer_price.textContent = "Total: " + total + "kr"

    cart_list.appendChild(footer_price);
    let checkout_link = document.createElement("a")
    let checkout_btn = document.createElement("button");
    checkout_btn.textContent = "Checkout"
    checkout_btn.style = "width: 100px; background-color: orange;"

    checkout_link.href = "/home/cart"
    
    checkout_link.appendChild(checkout_btn);
    cart_list.appendChild(checkout_link);
}


const deletepizza = (id) => {
    //delete one pizza in cart
    const index = cart.findIndex((obj) => obj.id === id);
    if (index > -1) {
        cart.splice(index, 1);
    }
    displayCart()
    console.log("delete ein pizza")
}

const deletecart = () => {
    //delete all pizzas in cart
    cart = []
    displayCart()
    console.log("delete cart")
}