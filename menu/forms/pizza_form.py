from django.forms import ModelForm, widgets
from django import forms
from menu.models import Pizza

class PizzaCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={ 'class': 'from-control' }))
    sales = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={ 'class': 'from-control' }))
    categories = forms.ModelMultipleChoiceField(required=True, widgets=forms.TextInput(attrs={ 'class': 'form-control' }))
    toppings = forms.ModelMultipleChoiceField(required=True, widgets=forms.TextInput(attrs={ 'class': 'form-control' }))
    ratings = forms.ModelMultipleChoiceField(required=True, widgets=forms.NumberInput(attrs={ 'class': 'form-control' }))

    class Meta:
        model = Pizza
        exclude = [ 'id' ]
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'description': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'created_at': widgets.DateInput(attrs={ 'class': 'form-control', 'type': 'date', 'placeholder': 'yyyy-mm-dd'}),
            'is_new': widgets.CheckboxInput(attrs={ 'class': 'checkbox' }),
            'price_small': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'price_medium': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'price_large': widgets.NumberInput(attrs={ 'class': 'form-control' }),
        }