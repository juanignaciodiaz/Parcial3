from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('prueba/', views.prueba, name='prueba'),
]
