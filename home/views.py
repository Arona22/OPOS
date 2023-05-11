from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def cart(request):
    return render(request, 'home/cart.html')

def thank(request):
    return render(request, 'home/thank.html')

def about(request):
    return render(request, 'home/about.html')

def terms(request):
    return render(request, 'home/terms.html')

def policy(request):
    return render(request, 'home/policy.html')