# Generated by Django 2.2.5 on 2019-09-27 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cita', '0006_auto_20190926_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (2, 'Cancelado'), (3, 'No Asistio')], default=1, verbose_name='Estado'),
        ),
    ]
