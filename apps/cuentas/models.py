from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    # fecha_nacimiento = models.DateTimeField('Fecha de nacimiento:')
    numero = models.IntegerField('precio', blank=False, null=False, default=0)
    imagen = models.ImageField('Imagen perfil:', upload_to='perfil', blank=False, null=False, default="")

    def idPerfil(self):
        return self.id

    def __str__(self):
        return self.usuario.username
@receiver(post_save, sender=User)
def actualizar_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario = instance)
    instance.perfil.save()