from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/pizza
    path('', views.index, name="pizza-index"),
]