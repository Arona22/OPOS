from django.forms import ModelForm, widgets
from menu.models import Pizza, Category, Topping
from django import forms

class PizzaCreateForm(ModelForm):
    image = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={ 'class': 'from-control' }))

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(), 
        required=True, 
        widget=forms.CheckboxSelectMultiple(attrs={ 'class': 'form-control' }))
    
    toppings = forms.ModelMultipleChoiceField(
        queryset=Topping.objects.all(), 
        required=True, 
        widget=forms.CheckboxSelectMultiple(attrs={ 'class': 'form-control' }))

    class Meta:
        model = Pizza
        exclude = [ 'id', 'ratings' ]
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'description': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'created_at': widgets.DateInput(attrs={ 'class': 'form-control', 'type': 'date', 'placeholder': 'yyyy-mm-dd'}),
            'is_new': widgets.CheckboxInput(attrs={ 'class': 'checkbox' }),
            'price_small': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'price_medium': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'price_large': widgets.NumberInput(attrs={ 'class': 'form-control' }),
        }