from apps.producto.models import Categoria, Producto
from apps.producto.forms import FormularioCategoria, FormularioProducto
from django.shortcuts import redirect, render

# Create your views here.
def productos(request):
    productos_encontrados = Producto.objects.all()
    categoria_encontradas = Categoria.objects.all()
    prueba = 'hola'
    context = {
        'productos': productos_encontrados,
        'categorias': categoria_encontradas
    }
    return render(request, 'pages/productos.html', context)

def filtroCategoria(request, idCategoria):
    productos_encontrados = Producto.objects.filter(categoria_id = idCategoria)
    categoria_encontradas = Categoria.objects.all()
    context = {
        'productos': productos_encontrados,
        'categorias': categoria_encontradas
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
    formularioCategoria = FormularioCategoria()

    if request.method == "POST":
        formulario = FormularioProducto(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('crudproducto')
    context = {
        'formulario': formulario ,
        'productos': productos_encontrados
    }
    return render(request, 'pages/crear_producto.html', context)

def crudCategoria(request):
    formulario = FormularioCategoria()
    if request.method == "POST":
        formulario = FormularioCategoria(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('categoria')

    context = {
        'formulario': formulario
    }
    return render(request, 'pages/crudCategoria.html', context)