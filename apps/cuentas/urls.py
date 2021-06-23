from django.contrib.auth.forms import AuthenticationForm
from django.urls import path
from django.contrib.auth.views import LoginView

from . import views
from .forms import IniciarSesion

urlpatterns = [
    path('registrarse/', views.registro, name='registrarse'),
    path('inicio-sesion/', LoginView.as_view(
        template_name='pages/inicio_sesion.html', authentication_form = IniciarSesion), 
        name='inicio-sesion'),
    path('salir/', views.salir, name='salir')
]

