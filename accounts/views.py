from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistration, UserLogin
from django.http import HttpResponse
import json
from django.contrib import messages
from user_profile.models import UserProfile
#

def login_view(request):
    return render(request, 'templates/registration/login.html')


def register_login(request):
    change = "active show"
    change2 = "active"
    login_url = 'registration/login.html'
    login_form = UserLogin(request.POST or None)
    register_form = UserRegistration(request.POST or None)
    if request.method == 'POST':

        if request.POST.get('form_type') == 'login' and login_form.is_valid():
            username, password = login_form.cleaned_data['username'], login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('user_profile:profile_detail_view')
                else:
                    return render(request, login_url, {'login_form': login_form, 'register_form': register_form})
            else:
                change = "active show"
                change2 = "active"
                messages.add_message(request, messages.ERROR, 'نام کاربری یا رمز عبور اشتباه است')
                return render(request, login_url, {'login_form': login_form, 'register_form': register_form, 'change':change, 'change2': change2})
        else:
            register_form = UserRegistration(request.POST)
            if register_form.is_valid():
                new_user = register_form.save()
                UserProfile.objects.create(user=new_user)
                return render(request, 'registration/register_done.html', {'new_user': new_user})
            else:
                change = None
                change2 = None
    return render(request, login_url, {'register_form': register_form, 'login_form': login_form, 'change':change, 'change2': change2})

