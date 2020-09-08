from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.blog, name="main"),
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]