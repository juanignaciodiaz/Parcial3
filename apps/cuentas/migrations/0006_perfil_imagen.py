# Generated by Django 3.2.3 on 2021-07-02 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0005_perfil_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='imagen',
            field=models.ImageField(default='', upload_to='perfil', verbose_name='Imagen perfil:'),
        ),
    ]
