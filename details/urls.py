from django.urls import path, include
from . import views

app_name = 'details'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_us, name="about_us"),
    #path('contanct/', views.contact_us, name="contact_us"),
    path('contact/', views.feedback, name='contact_us'),
]
