from django import forms
from .models import ContactUsMessage
from django.forms.widgets import TextInput

class ContactUsForm(forms.ModelForm):
    name = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'نام *'}))
    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={'placeholder':'ایمیل *'}))
    phone_number = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'شماره تلفن همراه'}))
    subject = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'موضوع پیام'}))
    body = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'متن پیام شما *'}))

    class Meta:
        model = ContactUsMessage
        fields = ('name', 'email', 'phone_number', 'subject', 'body')