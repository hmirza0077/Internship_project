from .models import Order
from django import forms
from django.utils.translation import gettext_lazy as _

class OrderForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': _('نام')}))
    last_name = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': _('نام خانوادگی')}))
    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={'placeholder':_('ایمیل')}))
    address = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': _('آدرس')}))
    postal_code = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': _('کد پستی')}))
    city = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': _('شهر')}))
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address', 'postal_code', 'city')