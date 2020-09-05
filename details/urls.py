from django.urls import path, include
from . import views

app_name = 'details'

urlpatterns = [
    path('home/', views.home, name='home'),
]
