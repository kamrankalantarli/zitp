from django.conf.urls import url
from .views import *

app_name = "kurs"

urlpatterns = [

    url(r'^index/$', index, name='kurs'),
    url(r'^(?P<id>\d+)/detail/$', detail, name='detail'),


]