from areas.models import Area
from cargos.models import Cargo
from django.contrib.auth.models import User
from django.db import models
from empresas.models import Empresa
from sedes.models import Sede


# Create your models here.
class Empleado(models.Model):
    id_emp = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=20, verbose_name='DNI')
    apellido_pat = models.CharField(max_length=50, verbose_name='Apellido paterno')
    apellido_mat = models.CharField(max_length=50, verbose_name='Apellido materno')
    nombres = models.CharField(max_length=50, verbose_name='Nombres')
    correo_e = models.CharField(max_length=50, verbose_name='Correo electrónico')
    celular = models.CharField(max_length=15, verbose_name='Numero celular')
    area = models.ForeignKey(Area, null=True, blank=True, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, null=True, blank=True, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, null=True, blank=True, on_delete=models.CASCADE)
    sede = models.ForeignKey(Sede, null=True, blank=True, on_delete=models.CASCADE)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Usuario')

    def __str__(self):
        fila = "DNI: " + self.dni + " - " + "Nombres: " + self.nombres
        return fila