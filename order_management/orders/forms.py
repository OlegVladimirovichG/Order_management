from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'status']


class DeleteOrderForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
