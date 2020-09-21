from .models import Order
from django import forms

class OrderForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': 'نام'}))
    last_name = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی'}))
    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={'placeholder':'ایمیل'}))
    address = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': 'آدرس'}))
    postal_code = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': 'کد پستی'}))
    city = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': 'شهر'}))
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address', 'postal_code', 'city')