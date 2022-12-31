from django.db import models

# Create your models here.
class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=100, verbose_name='Nombre')
    
    def __str__(self):
        fila = str(self.id_empresa) + " - " + self.nombre_empresa
        return fila