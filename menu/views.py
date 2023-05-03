from django.shortcuts import render

pizzas = [
    {
        "id": 0,
        "name": "Margarita",
        "toppings": ["tomato sauce", "cheese"],
        "price": {
            "small": 1199,
            "medium": 2199,
            "large": 3199
        }
    },
    {
        "id": 1,
        "name": "OPOS Special",
        "toppings": ["tomato sauce", "cheese", "pepperoni", "ham", "salami", "cream cheese", "cheddar"],
        "price": {
            "small": 1199,
            "medium": 2199,
            "large": 3199
        }
    },
    {
        "id": 2,
        "name": "Margarita",
        "toppings": ["tomato sauce", "cheese"],
        "price": {
            "small": 1199,
            "medium": 2199,
            "large": 3199
        }
    }
]

# Create your views here.
def index(request):
    return render(request, 'menu/index.html')
