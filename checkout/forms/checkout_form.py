from django.forms import ModelForm, widgets
from checkout.models import *

class Contact_info_form(ModelForm):
    class Meta:
        model = ContactInfo
        exclude = ['id', 'customer']
        widgets = {
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip_code': widgets.TextInput(attrs={'class': 'form-control'}),            
        }
        
class payment_form(ModelForm):
    class Meta:
        model = Payment
        exclude = ['id', 'pament_date', 'amount', 'customer']
        widgets = {
            'cardholder_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_month': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_year': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_cvv': widgets.TextInput(attrs={'class': 'form-control'}),           
        }
