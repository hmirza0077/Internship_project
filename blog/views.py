from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms


def blog(request):
    return render(request, 'blog/blog.html')

