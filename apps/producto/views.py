from apps.producto.models import Producto
from apps.producto.forms import FormularioCategoria, FormularioProducto
from django.shortcuts import redirect, render

# Create your views here.
def productos(request):
    productos_encontrados = Producto.objects.all()
    context = {
        'productos': productos_encontrados
    }
    return render(request, 'pages/productos.html', context)

def formularioPrueba(request):
    formulario = FormularioProducto
    context = {
        'formulario': formulario
    }
    return render(request, 'pages/prueba.html', context)

def agregarProducto(request):
    productos_encontrados = Producto.objects.all()
    formulario = FormularioProducto()

    if request.method == "POST":
        formulario = FormularioProducto(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('crudproducto')
    context = {
        'formulario': formulario ,
        'productos': productos_encontrados
    }
    return render(request, 'pages/crear_producto.html', context)