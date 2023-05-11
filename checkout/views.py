from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from checkout.forms.checkout_form import *

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
    
@login_required
def review(request):
    return render(request, 'checkout/review.html')

@login_required
def confirm(request):
    return render(request, 'checkout/confirm.html')


