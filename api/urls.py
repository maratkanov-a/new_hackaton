from django.conf.urls import url, include
from django.contrib import admin

from api.views import get_my_event, get_help

urlpatterns = [
    url(r'^get_events/', get_my_event, name='ny_events'),
    url(r'^get_help/', get_help, name='sos'),
]
