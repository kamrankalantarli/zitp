from django.conf.urls import url
from .views import *

app_name = "blog"

urlpatterns = [

    url(r'^index/$', index, name='blog'),
    url(r'^(?P<id>\d+)/detail/$', detail, name='detail'),

]

