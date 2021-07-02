from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('producto/', views.productos, name='producto'),
    path('categoria/', views.crudCategoria, name='categoria'),
    path('producto/<int:idCategoria>', views.filtroCategoria, name='filtro_categoria'),
    path('crear/', views.agregarProducto, name='crudproducto'),
    path('producto/agregado/<int:idProducto>', views.agregarCarrito, name='agregarCarrito'),
    path('crear/eliminar/<int:idProducto>', views.eliminarProducto, name='eliminarProducto'),
]