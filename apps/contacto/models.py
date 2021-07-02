from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
# class Trabajo(models.Model):
#     usuario = models.OneToOneField(User, on_delete=models.CASCADE)
#     rut = models.CharField('Ingrese su Rut' ,max_length=12, null=False, blank=False, unique=True)
#     cargo = models.CharField('Ingrese el cargo', max_length=17)
    
#     def __str__(self):
#         return self.usuario.username
#     @receiver(post_save, sender=User)
#     def agregar_perfil(sender, instance, created, **kwags):
#         if creado:
#             Trabajo.objects.create(usuario = instance)
#         instance.trabajo.save()
