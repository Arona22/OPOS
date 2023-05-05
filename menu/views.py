from django.shortcuts import render, get_object_or_404
from menu.models import Pizza


pizzas = [
    {
        "id": 0,
        "name": "Margarita",
        "image": "img/marga_pizza.jpg",
        "toppings": "tomato sauce and cheese",
        "price": {
            "small": 1199,
            "medium": 2199,
            "large": 3199
        },
        "type": ["popular"]
    },
    {
        "id": 1,
        "name": "OPOS Special",
        "image": "img/opos_pizza.jpg",
        "toppings": "tomato sauce, cheese, pepperoni, ham, salami, cream cheese, cheddar",
        "price": {
            "small": 1199,
            "medium": 2199,
            "large": 3199
        },
        "type": ["popular", "spicy", "new"]
    },
    {
        "id": 2,
        "name": "Pepperioni pizza",
        "image": "img/pep_pizza.jpg",
        "toppings": "tomato sauce, cheese, pepperoni",
        "price": {
            "small": 1199,
            "medium": 2199,
            "large": 3199
        },
        "type": ["spicy"]
    },
    {
        "id": 3,
        "name": "OPOS Special",
        "image": "img/opos_pizza.jpg",
        "toppings": "tomato sauce, cheese, pepperoni, ham, salami, cream cheese, cheddar",
        "price": {
            "small": 1199,
            "medium": 2199,
            "large": 3199
        },
        "type": ["popular", "spicy", "new"]
    }
]

# Create your views here.
def index(request):
    return render(request, 'menu/index.html', context={ 'pizzas': pizzas })

def create_pizza(request):
    if request.method == 'POST':
        print(1)
    else:
        print(2)
    return render(request, 'pizza')
