from django.shortcuts import redirect, render
from .forms import ComentarioBarra

def comentario(request):
    formulario = ComentarioBarra
    if request.method == "POST":
        formulario = ComentarioBarra(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('comentarios')

    context = {
        'formulario': formulario
    }
    return render(request, 'pages/comentarios.html', context)