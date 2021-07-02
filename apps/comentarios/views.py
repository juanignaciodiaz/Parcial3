from apps.comentarios.models import Comentario
from apps.cuentas.models import Perfil
from django.shortcuts import redirect, render
from .forms import ComentarioBarra
from django.contrib import messages

def comentario(request):
    comentarios = Comentario.objects.all()
    formulario = ComentarioBarra
    if request.method == "POST":
        # formulario = ComentarioBarra(perfil=request.user.id,
        # descripcion = request.POST.get('descripcion'))

        comentario = Comentario.objects.create(perfil = Perfil.objects.get(usuario = request.user.id), 
        descripcion = request.POST['descripcion'])
        # if comentario.is_valid():
            # formulario.save()
        comentario.save()
        return redirect('comentarios')

    context = {
        'formulario': formulario,
        'comentarios': comentarios
    }
    return render(request, 'pages/comentarios.html', context)