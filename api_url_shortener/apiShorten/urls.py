from django.urls import path
from . import views

urlpatterns = [
    path('apiShorten/', views.home, name='apiShorten'),
]