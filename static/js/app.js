
let cart = []

const get_cart = () => {
    cart = JSON.parse(localStorage.getItem('myArray'));
    
    if (cart === null){
        console.log("empty cart")
        cart = []
    }else {
        console.log(cart)
    }
}

const add_offer_cart = (name, img) => {

    //2for1
    let obj = {
        "name": name,
        "image": img
    }

    cart.push(obj);
    if (cart.length > 2){
        cart[cart.length - 2].price = 0
    }
    localStorage.setItem('myArray', JSON.stringify(cart));
    console.log("offer in cart: " + name + img)
}


const add_cart = (id, name, img) => {
    const sizeGroup = document.querySelector('.pizza-size');
    const selectedSize = sizeGroup.querySelector('input[name="size"]:checked');
    const selectedValue = selectedSize.id;
    
    let obj = {
        "id": id,
        "name": name,
        "image": img,
        "price": selectedValue,
        "quantity": 1
    }

    for (let i = 0; i < cart.length; i++) {
        if (cart[i].id == obj.id && cart[i].price == obj.price) {
            cart[i].quantity += 1
            localStorage.setItem('myArray', JSON.stringify(cart));
            return
        }
        console.log(cart[i])
    }
    cart.push(obj);
    localStorage.setItem('myArray', JSON.stringify(cart));
}



const displayCart = () => {
    get_cart()
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
        if (cart[i].name == "2for1" || cart[i].name == "10%"){
            //display offer in cart
            let pizzaItem = document.createElement("li");

            let pizzaName = document.createElement("h4");
            let pizzaImg = document.createElement("img");
            let pizzaex = document.createElement("button")

            pizzaItem.id = "pizzaitem"
            pizzaName.textContent = cart[i].name;

            pizzaImg.src = "/static/" + cart[i].image;
            pizzaImg.id = "cart_img"

            
            pizzaex.className = "pizzaex"
            pizzaex.onclick = () => deletepizza(cart[i].id);

            pizzaItem.appendChild(pizzaName);
            pizzaItem.appendChild(pizzaImg);
            pizzaItem.appendChild(pizzaex);

            cart_list.appendChild(pizzaItem);
            
        }else{
            //display pizza in cart
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
            
            pizzaquant.id = cart[i].name + cart[i].price
            pizzaquant.value = cart[i].quantity
            pizzaquant.type = "number"
            pizzaquant.style = "width: 50px; margin-right: 100px; margin-left: 5px; margin-top: 5px;"
            
            pizzaPrice.textContent = cart[i].price + "kr"

            pizzaItem.appendChild(pizzaName);
            
            pizzaItem.appendChild(pizzaPrice);
            pizzaItem.appendChild(pizzaImg);
            
            pizzaItem.appendChild(pizzaquant);
            pizzaItem.appendChild(pizzaex);

            cart_list.appendChild(pizzaItem);

            total += cart[i].price * cart[i].quantity

            //functionality for quantity
            const input = document.getElementById(cart[i].name + cart[i].price);
            input.addEventListener("change", updateValue);
            function updateValue(e) {
            cart[i].quantity = Number(e.target.value);
            localStorage.setItem('myArray', JSON.stringify(cart));
            }

        }
    }

    let footer_price = document.createElement("h3");
    footer_price.textContent = "Total: " + total + "kr"

    cart_list.appendChild(footer_price);
    let checkout_link = document.createElement("a")
    let checkout_btn = document.createElement("button");
    checkout_btn.textContent = "Checkout"
    checkout_btn.style = "width: 100px; background-color: orange;"

    checkout_link.href = "/checkout/contact_info"
    
    checkout_link.appendChild(checkout_btn);
    cart_list.appendChild(checkout_link);
}


const deletepizza = (id) => {
    //delete one pizza in cart
    const index = cart.findIndex((obj) => obj.id === id);
    if (index > -1) {
        cart.splice(index, 1);
    }
    localStorage.setItem('myArray', JSON.stringify(cart));
    displayCart()
    console.log("delete one pizza")
}

const deletecart = () => {
    //delete all pizzas in cart
    localStorage.setItem('myArray', JSON.stringify([]));
    displayCart()
    console.log("delete cart")
}


const checkout_cart = () => {
    console.log(cart)
    get_cart()
    let panel = document.getElementById("panel");
    panel.innerHTML='';

    for (let i = 0; i < cart.length; i++) {
        // PIZZAS

        //make box
        let checkItem = document.createElement("div");
        checkItem.style = "border-bottom: 1px solid; padding-bottom: 10px; padding-left: 10px;"
        checkItem.className = "form-group"


        //make img div
        let checkimgdiv = document.createElement("div");
        checkimgdiv.className = "col-sm-3 col-xs-3"
        checkItem.appendChild(checkimgdiv);

        //make img
        let checkimg = document.createElement("img");
        checkimgdiv.className = "img-responsive"
        checkimg.src =  "/static/" + cart[i].image;
        checkimg.style = "width: 100px; height: 100px;"
        checkimgdiv.appendChild(checkimg)


        //make product div
        let checkproddiv = document.createElement("div");
        checkproddiv.className = "col-sm-6 col-xs-6"
        checkItem.appendChild(checkproddiv)

        //make product name
        let checkprodname = document.createElement("div");
        checkprodname.className = "col-xs-12"
        checkprodname.textContent = cart[i].name
        checkprodname.style = "font-size: 20px;"
        checkproddiv.appendChild(checkprodname)

        //make product quantity
        let checkprodquan = document.createElement("div");
        checkprodquan.className = "col-xs-12"
        checkprodquan.textContent = "Quantity:" + cart[i].quantity
        checkproddiv.appendChild(checkprodquan)

        //make price div
        let checkpricediv = document.createElement("div");
        checkpricediv.className = "col-sm-3 col-xs-3 text-right"
        checkItem.appendChild(checkpricediv)

        //make price
        let checkprice = document.createElement("h4");
        checkprice.textContent = (cart[i].price * cart[i].quantity) + "kr"
        checkpricediv.appendChild(checkprice)



        //add box to panel
        panel.appendChild(checkItem);

    }
    //make spacer

    //make order total form
    let checktotalform = document.createElement("div");
    checktotalform.className = "form-group"
    checktotalform.style = "display: flex;"
    panel.appendChild(checktotalform);

    //make order total div
    let checktotaldiv = document.createElement("div");
    checktotaldiv.className = "col-xs-12"
    checktotaldiv.textContent = "Order tortal: "
    checktotaldiv.style = "font-size: 25px; padding-top: 18px;"
    checktotalform.appendChild(checktotaldiv);

    //make order total
    let checkout_total_final = 0
    for (let i = 0; i < cart.length; i++) {
        checkout_total_final += cart[i].price * cart[i].quantity
    }
    let checktotal = document.createElement("h3");
    checktotal.textContent = checkout_total_final + "kr"
    checktotal.style = "padding-right: 15px;"
    checktotalform.appendChild(checktotal);
}


