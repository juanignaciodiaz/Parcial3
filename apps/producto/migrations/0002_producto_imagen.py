# Generated by Django 3.2.3 on 2021-06-14 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.CharField(default='https://media.tenor.com/images/965beb93fefb499a174d45bfcef23c30/tenor.gif', max_length=150, verbose_name='Imagen'),
        ),
    ]
