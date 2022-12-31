# Generated by Django 4.1.4 on 2022-12-11 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id_doc', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_doc', models.CharField(max_length=50, verbose_name='Tipo documento')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha inicio')),
                ('fecha_final', models.DateField(verbose_name='Fecha final')),
                ('fecha_retorno', models.DateField(verbose_name='Fecha retorno')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripción')),
                ('estado_doc', models.CharField(max_length=50, verbose_name='Estado documento')),
            ],
        ),
    ]