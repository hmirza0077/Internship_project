from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class UserProfileForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': _('شماره تلفن همراه')}))
    postal_code = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': _('کد پستی')}))
    address = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': _('آدرس')}))
    home_telephone = forms.CharField(max_length=50, label=False, required=False, widget=forms.TextInput(attrs={'placeholder': _('شماره تلفن ثابت')}))
    city = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': _('شهر')}))
    gender = forms.CharField(max_length=50, label=False, required=False, widget=forms.TextInput(attrs={'placeholder': _('جنسیت')}))
    photo = forms.ImageField(label=False, required=False, widget=forms.TextInput(attrs={'placeholder': _('عکس پروفایل')}))
    class Meta:
        model = UserProfile
        fields = ('phone_number', 'postal_code', 'address', 'home_telephone', 'city', 'gender', 'photo')

class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': _('نام')}))
    last_name = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': _('نام خانوادگی')}))
    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={'placeholder':_('ایمیل')}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')