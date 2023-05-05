from django.shortcuts import render, get_object_or_404
import json
from menu.models import Pizza



# Create your views here.
def index(request):
    pizza_json = request.GET.get("pizza")
    pizza = json.loads(pizza_json)
    return render(request, 'pizza/index.html')


def get_pizza_by_id(request, id):
    return render(request, 'pizza/index.html', {
        'candy': get_object_or_404(Pizza, pk = id)
    })