from django.forms import ModelForm, widgets
from django import forms
from edit_profile.models import User

class UserUpdateName(ModelForm):
    class Meta:
        model = User
        exclude = [ 'id', 'email', 'phone', 'password', 'proimg' ]
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control' }),
        }

class UserUpdateEmail(ModelForm):
    class Meta:
        model = User
        exclude = [ 'id', 'name', 'phone', 'password', 'proimg' ]
        widgets = {
            'email': widgets.TextInput(attrs={ 'class': 'form-control' }),
        }


class UserUpdatePhone(ModelForm):
    class Meta:
        model = User
        exclude = [ 'id', 'name', 'email', 'password', 'proimg' ]
        widgets = {
            'phone': widgets.TextInput(attrs={ 'class': 'form-control' }),
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