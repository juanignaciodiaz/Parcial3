from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import widgets

class FormularioRegistro(UserCreationForm):
    fecha_nacimiento = forms.DateField( widget= forms.TextInput( attrs={ 'type': 'date'}))
    imagen = forms.FileField()
    admin = forms.BooleanField()

    def __init__(self, *args, **kwargs):
        super(FormularioRegistro, self).__init__(*args, **kwargs)
        for campovisible in self.visible_fields():
            campovisible.field.widget.attrs['class'] = 'formulario-registro-login'
            
    class Meta:
        model = User
        # widgets = {
        #     'admin': forms.CheckboxInput(attrs={'class':'form-control'})
        # }
        fields = ('username', 'first_name', 'last_name', 'email', 'admin','imagen', 'password1', 'password2')

class IniciarSesion(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(IniciarSesion, self).__init__(*args, **kwargs)
        for campovisible in self.visible_fields():
            campovisible.field.widget.attrs['class'] = 'formulario-registro-login'

    class Meta:
        fields = ('username', 'password')