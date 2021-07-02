from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import fields

class FormularioRegistro(UserCreationForm):
    fecha_nacimiento = forms.DateField( widget= forms.TextInput( attrs={ 'type': 'date'}))
    imagen = forms.FileField()
    def __init__(self, *args, **kwargs):
        super(FormularioRegistro, self).__init__(*args, **kwargs)
        for campovisible in self.visible_fields():
            campovisible.field.widget.attrs['class'] = 'formulario-registro-login'
            
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'imagen', 'password1', 'password2')

class IniciarSesion(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(IniciarSesion, self).__init__(*args, **kwargs)
        for campovisible in self.visible_fields():
            campovisible.field.widget.attrs['class'] = 'formulario-registro-login'

    class Meta:
        fields = ('username', 'password')