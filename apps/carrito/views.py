from apps.producto.models import Producto
from django.contrib.auth.models import User
from apps.cuentas.models import Perfil
from apps.carrito.models import Carrito
from django.shortcuts import redirect, render
from django.db.models import Sum

# Create your views here.

def carrito(request):
    total = 0
    
    perfil = Perfil.objects.get(usuario = User.objects.get(id = request.user.id))
    productos = Carrito.objects.filter(usuario = perfil.id)
    for producto in productos:
        total = total + producto.producto.precio
    context = {
        'productos': productos,
        'perfil': perfil,
        'total': total
    }
    return render(request, 'pages/carrito.html', context)

def eliminarCarrito(request, idCarrito):
    producto = None
    try:
        producto = Carrito.objects.get(id = idCarrito)
        producto.delete()
    except:
        pass
    return redirect('carrito')