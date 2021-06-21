from apps.producto.models import Producto
from django.shortcuts import render

# Create your views here.
def principal(request):
    productos = Producto.objects.all()
    context = {
        "productos": productos
    }
    return render(request, 'pages/principal.html', context)