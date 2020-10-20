from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from shop.models import Product
from django.contrib.auth.models import User


def home(request):
    latest_products = Product.objects.all()[:10]
    context = {'products': latest_products}
    return render(request, 'details/home.html', context=context)

def about_us(request):
    user = User.objects.all()
    context = {'user': user}
    return render(request, 'details/about.html', context=context)

def feedback(request):
    if request.method == 'POST':
        feedback = forms.ContactUsForm(request.POST)
        if feedback.is_valid():
            feedback.save()
            messages.add_message(request, messages.INFO, 'ممنون از اینکه نظرات خود را با ما در میان میگذارید.')
            return redirect('details:contact_us')
    else:
        feedback = forms.ContactUsForm()
    return render(request, 'details/contact.html', {'feedback': feedback})