# Generated by Django 4.1.4 on 2022-12-28 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0001_initial'),
        ('empleados', '0007_remove_empleado_status_alter_empleado_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='areas.area'),
        ),
    ]