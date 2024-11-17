from django.urls import path
from .views import shorten_url

urlpatterns = [
    path('api/shorten/', shorten_url, name='shorten_url'),
]