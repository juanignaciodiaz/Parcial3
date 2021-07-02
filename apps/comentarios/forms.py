from django import forms
from .models import Comentario

class ComentarioBarra(forms.ModelForm):
    class Meta:
        model = Comentario
        widgets = {
            'descripcion': forms.Textarea(attrs={"class":"form-control","placeholder":"Agregar comentario...","maxlength":"499","minlength":"19"})
        }
        fields = ('descripcion',)