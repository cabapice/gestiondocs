from django.db import models

# Create your models here.
class Area(models.Model):
    id_area = models.AutoField(primary_key=True)
    nombre_area =models.CharField(max_length=30, verbose_name='Nombre')

    def __str__(self):
        fila = str(self.id_area) + " - " + self.nombre_area
        return fila