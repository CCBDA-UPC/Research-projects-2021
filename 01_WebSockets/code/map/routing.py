# map/routing.py
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/map/$', consumers.MapConsumer.as_asgi()),
]