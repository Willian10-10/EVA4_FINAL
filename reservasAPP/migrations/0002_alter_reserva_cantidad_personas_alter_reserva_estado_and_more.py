# Generated by Django 5.0.1 on 2024-12-16 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservasAPP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='cantidad_personas',
            field=models.PositiveIntegerField(verbose_name='Cantidad de Personas'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='estado',
            field=models.CharField(choices=[('RESERVADO', 'Reservado'), ('COMPLETADA', 'Completada'), ('ANULADA', 'Anulada'), ('NO_ASISTEN', 'No Asisten')], max_length=15, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha',
            field=models.DateField(verbose_name='Fecha de la Reserva'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='hora',
            field=models.TimeField(verbose_name='Hora de la Reserva'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre del Cliente'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='observacion',
            field=models.TextField(blank=True, null=True, verbose_name='Observación'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='telefono',
            field=models.CharField(max_length=15, verbose_name='Teléfono'),
        ),
    ]
