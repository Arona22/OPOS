from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/checkout
    path('contact_info', views.contact_info, name="checkout-contact"),
    path('payment', views.payment, name="checkout-payment"),
    path('review', views.review, name="checkout-review"),
    path('confirm', views.confirm, name="checkout-confirm"),
]