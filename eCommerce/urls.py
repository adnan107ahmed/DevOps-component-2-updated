"""
eCommerce URL Configuration

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),

    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('search/', include('search.urls')),
    path('cart/', include('carts.urls')),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
