# Generated by Django 3.2.3 on 2021-07-02 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0003_alter_perfil_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
