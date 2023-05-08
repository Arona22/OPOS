from django.forms import ModelForm, widgets
from django import forms
from edit_profile.models import User

class UserCreateForm(ModelForm):
    class Meta:
        model = User
        exclude = [ 'id' ]
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'email': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'phone': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'password': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'proimg ': widgets.TextInput(attrs={ 'class': 'form-control' }),
        }