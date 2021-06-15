from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.prueba, name='prueba'),
    path('prueba/', views.formularioPrueba, name='formulario'),
    path('crear/', views.agregarProducto, name='crudproducto'),
]
