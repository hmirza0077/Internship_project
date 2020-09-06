from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': 'شماره تلفن همراه'}))
    postal_code = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': 'کد پستی'}))
    address = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': 'آدرس'}))
    home_telephone = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': 'شماره تلفن ثابت'}))
    city = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': 'شهر'}))
    gender = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': 'جنسیت'}))
    class Meta:
        model = UserProfile
        fields = ('phone_number', 'postal_code', 'address', 'home_telephone', 'city', 'gender')

class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': 'نام'}))
    last_name = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی'}))
    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={'placeholder':'ایمیل'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')