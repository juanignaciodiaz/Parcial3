# Generated by Django 3.2.3 on 2021-07-02 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0004_alter_perfil_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='numero',
            field=models.IntegerField(default=0, verbose_name='precio'),
        ),
    ]
