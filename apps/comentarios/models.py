from django.db import models
from apps.cuentas.models import Perfil

# Create your models here.
class Comentario(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    descripcion = models.TextField('Caja de Comentarios', max_length=199, blank=False, null=False)
    fecha = models.DateTimeField('Fecha de Subida', auto_now_add=True)