from apps.cuentas.models import Perfil
from apps.carrito.models import Carrito
from apps.producto.models import Categoria, Producto
from apps.producto.forms import FormularioCategoria, FormularioProducto
from django.shortcuts import redirect, render

# Create your views here.
def productos(request):
    productos_encontrados = Producto.objects.all()
    categoria_encontradas = Categoria.objects.all()
    # usuariom= Perfil.objects.get(usuario = request.user.id),
    context = {
        'productos': productos_encontrados,
        'categorias': categoria_encontradas,
        # 'usuariom':usuariom
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

def agregarCarrito(request, idProducto):
    productoCarrito = Carrito.objects.create(
        usuario= Perfil.objects.get(usuario = request.user.id),
        producto=Producto.objects.get(id = idProducto))
    # productoCarrito.save()
    return redirect('producto')

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

def eliminarProducto(request, idProducto):
    producto_encontrado = None

    try:
        producto_encontrado = Producto.objects.get(pk = idProducto)
        producto_encontrado.delete()
    except:
        pass
    return redirect('crudproducto')

def buscarProductoId(request, idProducto):
    try:
        producto_encontrado = Producto.objects.get(pk = idProducto)
    except:
        pass
    formularioP = FormularioProducto(instance= producto_encontrado)
    contexto = {
        'formulario': formularioP,
        'producto': producto_encontrado
    }
    return render(request, 'pages/editarProducto.html', contexto)

def editarProducto(request, idProducto):
    producto_encontrado = None
    try:
        producto_encontrado = Producto.objects.get(pk = idProducto)

    except:
        pass
    formulario_producto = FormularioProducto(request.POST, request.FILES, instance = producto_encontrado)
    
    if formulario_producto.is_valid():
        formulario_producto.save()
        return redirect('crudproducto')
