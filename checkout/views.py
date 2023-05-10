from django.shortcuts import render


# Create your views here.
def contact_info(request):
    return render(request, 'checkout/contact_info.html')

def payment(request):
    return render(request, 'checkout/payment.html')

def review(request):
    return render(request, 'checkout/review.html')

def confirm(request):
    return render(request, 'checkout/confirm.html')


