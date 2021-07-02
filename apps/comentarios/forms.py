from django import forms
from .models import Comentario

class ComentarioBarra(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'