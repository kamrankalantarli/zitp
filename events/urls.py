from django.conf.urls import url
from .views import *

app_name = "events"

urlpatterns = [

    url(r'^index/$', index, name='events'),
    url(r'^(?P<id>\d+)/detail/$', detail, name='detail'),


]