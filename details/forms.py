from django import forms
from .models import ContactUsMessage
from django.forms.widgets import TextInput
from django.utils.translation import gettext_lazy as _

class ContactUsForm(forms.ModelForm):
    name = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': _('نام *')}))
    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={'placeholder': _('ایمیل *')}))
    phone_number = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': _('شماره تلفن همراه')}))
    subject = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': _('موضوع پیام')}))
    body = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': _('متن پیام شما *')}))

    class Meta:
        model = ContactUsMessage
        fields = ('name', 'email', 'phone_number', 'subject', 'body')