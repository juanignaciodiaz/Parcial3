from django import forms
from django.contrib.auth.form import UserCreationForm


def agregarForControl(campos):
    for camposVisibles in campos:
        camposVisibles.field.widget.attrs['class'] = 'form-control'

class RegistroUsuario(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistroUsuario, self).__init__(*args, **kwargs)
        agregarFormControl(self.visible_field())

    rut = forms.CharField(max_length=12, help_text="Ingrese su rut")

    class Meta:
        model = User 
        fields = ('rut', 'nombre', 'apellido', 'telefono', 'correo_electronico', 'cargo') #()
