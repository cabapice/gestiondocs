from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Empleado
from .forms import EmpleadoForm
# Create your views here.

def empleados(request):
    empleados = Empleado.objects.all()    
    return render(request, 'empleado/index.html', {'empleados': empleados})
def crear_emp(request):
    formulario = EmpleadoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('empleados')
    return render(request, 'empleado/crear.html', {'formulario': formulario})
def editar_emp(request, id_emp):
    empleado = Empleado.objects.get(id_emp=id_emp)
    formulario = EmpleadoForm(request.POST or None, request.FILES or None, instance=empleado)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('empleados')
    return render(request, 'empleado/editar.html', {'formulario': formulario})
def eliminar_emp(request, id_emp):
    empleado = Empleado.objects.get(id_emp=id_emp)
    empleado.delete()
    return redirect('empleados')
