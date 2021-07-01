from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Perfil(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    # fecha_nacimiento = models.DateTimeField('Fecha de nacimiento:')
    # imagen = models.ImageField

    def idPerfil(self):
        return self.id

    def __str__(self):
        return self.usuario.username
@receiver(post_save, sender=User)
def actualizar_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario = instance)
    instance.perfil.save()