from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/menu
    path('', views.index, name="menu-index"),
    path('<int:id>', views.get_pizza_by_id, name="order-pizza")
]