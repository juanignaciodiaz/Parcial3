# Generated by Django 3.2.3 on 2021-07-02 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0006_perfil_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='imagen',
        ),
    ]
