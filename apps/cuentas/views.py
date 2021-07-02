from django.contrib.auth import logout
from apps.cuentas.forms import FormularioRegistro
from django.shortcuts import redirect, render

# Create your views here.
def prueba(request):
    formulario = FormularioRegistro()
    context = {
        'formulario': formulario
    }

    return render(request, 'pages/prueba.html', context)

def registro(request):
    formulario = None
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST, request.FILES)
        if formulario.is_valid():
            usuario = formulario.save()
            usuario.refresh_from_db()
            # usuario.perfil.imagen = formulario.cleaned_data.get('imagen')
            usuario.perfil.imagen = request.FILES['imagen'] 
            # usuario.perfil.fecha_nacimiento = formulario.cleaned_data.get('fecha_nacimiento')
            usuario.save()
            return redirect('principal')
    if request.method == 'GET':
        formulario = FormularioRegistro()

    contexto = {
        'formulario': formulario
    }

    return render(request, 'pages/registrar.html', contexto)

def inicio_sesion(request):
    return render(request, 'pages/inicio_sesion.html')

def salir(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('producto')