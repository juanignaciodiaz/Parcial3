from django.urls import path
from . import views
urlpatterns = [
    path('carrito/', views.carrito, name='carrito'),
    path('eliminar/<int:idCarrito>', views.eliminarCarrito, name='eliminarCarrito'),
]
