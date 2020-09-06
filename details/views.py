from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms


def home(request):
    return render(request, 'details/home.html')

def about_us(request):
    return render(request, 'details/about.html')

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