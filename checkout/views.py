from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from checkout.forms.checkout_form import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
from .models import Order
from user.models import Profile



# Create your views here.
@login_required
def contact_info(request):
    if request.method == 'POST':
        form = Contact_info_form(data=request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('checkout-payment')      
    else:
        form = Contact_info_form()
    return render(request, 'checkout/contact_info.html', {
        'form': form
    })

@login_required
def payment(request):
    if request.method == 'POST':
        form = payment_form(data=request.POST)
        if form.is_valid():
            payment = form.save()
            return redirect('checkout-review')      
    else:
        form = payment_form()
    return render(request, 'checkout/payment.html', {
        'form': form
    })
    
@csrf_exempt
def review(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8')) # decode the request body and convert to dictionary
        data['product'] = int(data['product']) # convert product field to integer
        pizza = Pizza.objects.get(id=data['product']) # retrieve the Pizza instance based on the product ID
        data['product'] = pizza
        customer = Profile.objects.get(user=request.user) # retrieve the current customer based on the logged-in user
        data['customer_id'] = customer.id
        your_model_instance = Order.objects.create(**data) # create and save an instance of the Order model using the data
        return HttpResponse(status=200) # return a success response
    return render(request, 'checkout/review.html')

@login_required
def confirm(request):
    return render(request, 'checkout/confirm.html')


