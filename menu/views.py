from django.shortcuts import render, get_object_or_404, redirect
from menu.models import Pizza, PizzaImage
from .forms.pizza_form import PizzaCreateForm
from django.http import HttpResponse, JsonResponse



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
    

    if 'category_filter' in request.GET:
        filter = request.GET[ 'category_filter' ]
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
            'categories': [category.category.name for category in x.pizza_category_set.all()],
        } for x in Pizza.objects.all()]
        returned_pizzas = []
        for i in range(len(pizzas)):
            if filter in pizzas[i]['categories']:
                returned_pizzas.append(pizzas[i])

        return JsonResponse({ 'data': returned_pizzas })
    
    if 'order_by_price' in request.GET:
        return render(request, 'menu/index.html', context={ 'pizzas': Pizza.objects.all().order_by('id') })

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
