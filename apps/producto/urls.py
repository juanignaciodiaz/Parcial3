from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('producto/', views.productos, name='producto'),
    path('crear/', views.agregarProducto, name='crudproducto'),
]
