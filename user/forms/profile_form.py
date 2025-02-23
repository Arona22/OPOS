from django.forms import ModelForm, widgets
from user.models import Profile

class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = [ 'id', 'user' ]
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'email': widgets.TextInput(attrs={ 'class': 'form-control'}),
            'phone': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'profile_image': widgets.TextInput(attrs={ 'class': 'form-control' }),
        }