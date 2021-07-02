from django.db import models
from apps.cuentas.models import Perfil

# Create your models here.
class Comentario(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    descripcion = models.TextField('Descripción', max_length=199, blank=False, null=False)
    fecha = models.DateTimeField(auto_now_add=True)