from apps.producto.models import Producto
from apps.producto.forms import FormularioCategoria, FormularioProducto
from django.shortcuts import render

# Create your views here.
def prueba(request):
    return render(request, 'layout/layout.html')

def formularioPrueba(request):
    formulario = FormularioProducto
    context = {
        'formulario': formulario
    }
    return render(request, 'pages/prueba.html', context)

def agregarProducto(request):
    productos_encontrados = Producto.objects.all()
    formulario = FormularioProducto
    # id_max = Producto.objects.
    context = {
        'formulario': formulario ,
        'productos': productos_encontrados
    }
    return render(request, 'pages/crear_producto.html', context)