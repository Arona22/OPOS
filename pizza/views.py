from django.shortcuts import render, get_object_or_404
from menu.models import Pizza



# Create your views here.
def index(request):
    pizza = request.GET.get("pizza")
    return render(request, 'pizza/index.html')


def get_pizza_by_id(request, id):
    return render(request, 'pizza/index.html', {
        'candy': get_object_or_404(Pizza, pk = id)
    })