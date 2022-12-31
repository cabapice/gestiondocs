from django.db import models

from empleados.models import Empleado

# Create your models here.
class Documento(models.Model):
    id_doc = models.AutoField(primary_key=True)
    tipo_doc = models.CharField(max_length=50, verbose_name='Tipo documento')
    fecha_inicio = models.DateField(verbose_name='Fecha inicio')
    fecha_final = models.DateField(verbose_name='Fecha final')
    fecha_retorno = models.DateField(verbose_name='Fecha retorno')
    descripcion = models.TextField(verbose_name="Descripción", null=True)
    estado_doc = models.CharField(max_length=50, verbose_name='Estado documento')
    empleado = models.ForeignKey(Empleado, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        fila = "Id doc: " + str(self.id_doc) + " - " + "tipo doc: " + self.tipo_doc
        return fila