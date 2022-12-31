#from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin
from django import forms
from .models import Empleado, Area

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields ='__all__'
        """widgets = {
            'area': AutocompleteSelect(
                Area._meta.get_field('id_area').remote_field,
                admin.site,
                attrs={'placeholder': 'seleccionar...'},
            )
        }"""