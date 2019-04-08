"""Zitp URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from django.conf.urls.static import static
from django.conf import settings
from home.views import homel
from contact.views import Contact
from about.views import About
from blog.views import *
from events.views import *
from galeriya.views import *
from kurs.views import *


urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^$', homel , name='home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^galeriya/', include('galeriya.urls')),
    url(r'^kurs/', include('kurs.urls')),
    url(r'^contact/', Contact , name='contact'),
    url(r'^about/', About , name='about'),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)