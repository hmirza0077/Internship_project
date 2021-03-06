"""ikala URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls), # admin site
    path('accounts/', include('accounts.urls')),
    path('user_profile/', include('user_profile.urls')),
    path('payment/', include('payment.urls')),
    path('rosetta/', include('rosetta.urls')),
    path('coupons/', include('coupons.urls')),
    path('blog/', include('blog.urls')),
    path('shop/', include('shop.urls')),
    path('orders/', include('orders.urls')),
    path('cart/', include('cart.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('', include('details.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)