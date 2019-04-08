from django.conf.urls import url
from .views import *

app_name = "galeriya"

urlpatterns = [

    url(r'^index/$', index, name='galeiya'),
    url(r'^(?P<id>\d+)$', detail),


]