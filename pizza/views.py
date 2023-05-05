from django.shortcuts import render
import json


# Create your views here.
def index(request):
    pizza_json = request.GET.get("pizza")
    pizza = json.loads(pizza_json)
    return render(request, 'pizza/index.html')
