from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def contact_info(request):
    return render(request, 'checkout/contact_info.html')

@login_required
def payment(request):
    return render(request, 'checkout/payment.html')

@login_required
def review(request):
    return render(request, 'checkout/review.html')

@login_required
def confirm(request):
    return render(request, 'checkout/confirm.html')


