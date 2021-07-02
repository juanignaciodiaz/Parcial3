from apps.producto.models import Producto
from django.db.models.deletion import CASCADE, SET_NULL
from apps.cuentas.models import Perfil
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Carrito(models.Model):
    usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    cantidad = models.PositiveBigIntegerField(blank=True, null=True, default=1)