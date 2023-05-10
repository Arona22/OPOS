from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/home
    path('', views.index, name="home-index"),
    path('cart', views.cart, name="home-cart"),
    path('thank', views.thank, name="thank-index")
]