from django.shortcuts import render

offers = [
    {
        "id": 0,
        "name": "2for1",
        "description": "Get two pizzas for the price of one!",
        "img": "img/fish_pizza.jpg"
    },
        {
        "id": 1,
        "name": "jills",
        "description": "Get two pizzas for the price of one!",
        "img": "img/marga_pizza.jpg"
    },
        {
        "id": 2,
        "name": "kila",
        "description": "Get two pizzas for the price of one!",
        "img": "img/background.jpg"
    },
     
]

# Create your views here.
def index(request):
    return render(request, 'offers/index.html', context={'offers': offers})