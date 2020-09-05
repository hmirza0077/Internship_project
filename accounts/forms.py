from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm, SetPasswordForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth import get_user_model

#Login Form
class UserLogin(forms.Form):
    username = forms.CharField(label=False, widget=TextInput(attrs={'class':'validate','placeholder': 'نام کاربری یا ایمیل خود را وارد کنید...'}))
    password = forms.CharField(label=False, widget=PasswordInput(attrs={'placeholder': 'رمز عبور'}))


#Email Form
class CustomEmailForm(PasswordResetForm):
    email = forms.EmailField(label=False, max_length=254, widget=TextInput(attrs={'class':'validate','placeholder': 'ایمیل'}))


#Change pass Form
class CustomPassChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="", strip=False, widget=forms.PasswordInput(attrs={'autofocus': True, 'placeholder': 'رمز عبور قدیمی' }))
    new_password1 = forms.CharField(label="", strip=False, widget=forms.PasswordInput(attrs={'placeholder': "رمز عبور جدید"}))
    new_password2 = forms.CharField(label="", strip=False, widget=forms.PasswordInput(attrs={'placeholder':"تایید رمز عبور جدید"}))


#Resetpass Form
class CustomResetPassForm(SetPasswordForm):
    new_password1 = forms.CharField(label="", strip=False, widget=forms.PasswordInput(attrs={'placeholder': "رمز عبور جدید"}))
    new_password2 = forms.CharField(label="", strip=False, widget=forms.PasswordInput(attrs={'placeholder': "تایید رمز عبور جدید"}))


#user Registration Form
class UserRegistration(UserCreationForm):
    username = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))
    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={'placeholder':'ایمیل'}))
    password1 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': "رمز عبور"}))
    password2 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder':"تایید رمز عبور"}))

    class Meta:
	    model = get_user_model()
	    fields = ["username", "email", "password1", "password2"]

    #(Just sign up unique email(sign up with an email don't exist in database)
    def clean_email(self):
        cd = self.cleaned_data
        if get_user_model().objects.filter(email=cd['email']).exists():
            raise forms.ValidationError('قبلا با ایمیل ثبت نام انجام شده است')
        return cd['email']


#Create UserProfile Form
class PasswordResetRequestForm(forms.Form):
    mobile_phone = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'شماره تماس همراه'}))
