from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField('Nombre:', max_length=50, blank=False, null=False)
    descripcion = models.TextField('Descripción', max_length=150, blank=False, null=False)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField('Nombre Producto:', max_length=50, blank=False, null=False)
    precio = models.PositiveIntegerField('Precio:')
    stock = models.IntegerField('Stock:', blank=False, null=False)
    estadooferta = models.BooleanField('estadooferta:', default=0)
    descuento = models.PositiveSmallIntegerField('descuento:', default=0)
    fecha_creacion = models.DateTimeField('Fecha creacion:', auto_now_add=True)
    fecha_actualizacion = models.DateTimeField('Actualizado:', auto_now=True)
    imagen = models.ImageField('Imagen:', upload_to='productos', blank=False, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null = True)
