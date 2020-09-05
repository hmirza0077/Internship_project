from django.urls import path, include
from . import views

app_name = 'user_profile'

urlpatterns = [
    path('dashboard/', views.profile_detail_view, name='profile_detail_view'),
    path('dashboard/edit/', views.edit_profile, name='edit_profile'),
]
