from django.forms import ModelForm, widgets
from django import forms
from show_profile.models import User

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        exclude = [ 'id', 'password' ]
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'email': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'phone': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'proimg ': widgets.TextInput(attrs={ 'class': 'form-control' }),
        }



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