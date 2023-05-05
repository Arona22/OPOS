from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/pizza
    path('', views.index, name="pizza-index"),
    path('<int:id>', views.get_pizza_by_id, name='pizza-detailes')
]