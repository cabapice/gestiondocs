from django.db import models

# Create your models here.
class Cargo(models.Model):
    id_car = models.AutoField(primary_key=True)
    nombre_car = models.CharField(max_length=50, verbose_name='Nombre')

    def __str__(self):
        fila = str(self.id_car) + " - " + self.nombre_car
        return fila