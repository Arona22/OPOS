from django.shortcuts import render, get_object_or_404, redirect
from menu.models import Pizza, PizzaImage
from .forms.pizza_form import PizzaCreateForm
from django.http import HttpResponse, JsonResponse



def dumby_data():
    pass
    # pizzas = [
    #     {
    #         "id": 0,
    #         "name": "Margarita",
    #         "image": "img/marga_pizza.jpg",
    #         "toppings": "tomato sauce and cheese",
    #         "price": {
    #             "small": 1199,
    #             "medium": 2199,
    #             "large": 3199
    #         },
    #         "type": ["popular"]
    #     },
    #     {
    #         "id": 1,
    #         "name": "OPOS Special",
    #         "image": "img/opos_pizza.jpg",
    #         "toppings": "tomato sauce, cheese, pepperoni, ham, salami, cream cheese, cheddar",
    #         "price": {
    #             "small": 1199,
    #             "medium": 2199,
    #             "large": 3199
    #         },
    #         "type": ["popular", "spicy", "new"]
    #     },
    #     {
    #         "id": 2,
    #         "name": "Pepperioni pizza",
    #         "image": "img/pep_pizza.jpg",
    #         "toppings": "tomato sauce, cheese, pepperoni",
    #         "price": {
    #             "small": 1199,
    #             "medium": 2199,
    #             "large": 3199
    #         },
    #         "type": ["spicy"]
    #     },
    #     {
    #         "id": 3,
    #         "name": "OPOS Special",
    #         "image": "img/opos_pizza.jpg",
    #         "toppings": "tomato sauce, cheese, pepperoni, ham, salami, cream cheese, cheddar",
    #         "price": {
    #             "small": 1199,
    #             "medium": 2199,
    #             "large": 3199
    #         },
    #         "type": ["popular", "spicy", "new"]
    #     }
    # ]

# Create your views here.
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET[ 'search_filter' ]
        pizzas = [ {
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'created_at': x.created_at,
            'is_new': x.is_new,
            'price_small': x.price_small,
            'price_medium': x.price_medium,
            'price_large': x.price_large,
            'firstImage': x.pizzaimage_set.first().image,
        } for x in Pizza.objects.filter(name__icontains=search_filter) ]
        return JsonResponse({ 'data': pizzas })
    
    elif 'category_filter' in request.GET:
        filter = request.GET[ 'category_filter' ]
        pizzas = [ {
            'id': x.id,
            'name': x.name,
            'categories': x.categories,
            'description': x.description,
            'created_at': x.created_at,
            'is_new': x.is_new,
            'price_small': x.price_small,
            'price_medium': x.price_medium,
            'price_large': x.price_large,
            'firstImage': x.pizzaimage_set.first().image,
        } for x in Pizza.objects.filter(categories__contains=filter) ]
        return JsonResponse({ 'data': pizzas })


    return render(request, 'menu/index.html', context={ 'pizzas': Pizza.objects.all().order_by('name') })

def get_pizza_by_id(request, id):
    return render(request, 'menu/order_pizza.html', {
        'pizza': get_object_or_404(Pizza, pk=id)
    })

def create_pizza(request):
    if request.method == 'POST':
        form = PizzaCreateForm(data = request.POST)
        if form.is_valid():
            pizza = form.save()
            pizza_image = PizzaImage(image=request.POST['image'], pizza = pizza)
            pizza_image.save()
            return redirect('menu-index')
    else:
        form = PizzaCreateForm()
    return render(request, 'menu/create_pizza.html', {
        'form': form
    })
