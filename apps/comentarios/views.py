from django.shortcuts import redirect, render
from .forms import ComentarioBarra

def comentario(request):
    return render(request, 'pages/comentarios.html')