"""Rental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path, re_path
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.views.generic.base import RedirectView

admin.site.site_header = "Rental Admin"
admin.site.site_title = "Rental Admin Portal"
admin.site.index_title = "Welcome to Rental Admin Portal"

admin.autodiscover()
urlpatterns = [
    path('', RedirectView.as_view(url='/index/')),
    path('index/', views.index),
    path('home/', views.home),
    path('contact/', views.contact),
    path('about/', views.about),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('register', views.register),
    path('login', views.login_view),
    path('profile/', views.profile),
    path('post/', views.post),
    path('posth/', views.posth),
    path('logout', LogoutView.as_view()),
    path('descr/', views.descr),
    path('deleter', views.deleter),
    path('deleteh', views.deleteh),
    path('search/', views.search)
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
