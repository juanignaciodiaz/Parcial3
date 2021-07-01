from django.shortcuts import redirect, render

def comentario(request):
    return render(request, 'pages/comentarios.html')