# Generated by Django 3.2.3 on 2021-06-29 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='cantidad',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
