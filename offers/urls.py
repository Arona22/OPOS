from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/offers
    path('', views.index, name="offers-index"),
]