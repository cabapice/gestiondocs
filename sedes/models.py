from django.db import models

# Create your models here.
class Sede(models.Model):
    id_sede = models.AutoField(primary_key=True)
    nombre_sede = models.CharField(max_length=50, verbose_name='Nombre')  

    def __str__(self):
        fila = str(self.id_sede) + " - " + self.nombre_sede
        return fila