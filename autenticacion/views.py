from django.shortcuts import render, redirect
from django.views.generic import View

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'registro/inicio.html')

class crear_usuario(View):
    def get(self, request):
        form=UserCreationForm()
        return render(request,"registro/registro.html",{"form":form})

    def post(self, request):
        form=UserCreationForm(request.POST)
        if form.is_valid():            
            usuario=form.save()
            login(request, usuario)
            return redirect('../empleados/crear_emp')
        else:
            if request.POST['password1'] != request.POST['password2']:
                return render(request,"registro/registro.html",{
                    "form":form,
                    "error":'Contraseñas no coinciden.'
                    })
            return render(request,"registro/registro.html",{
                    "form":form,
                    "error":'La contraseña no es segura.'
                    })
            
def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'registro/iniciar_sesion.html', {
            'form': AuthenticationForm
        })
    else:
        usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:
            return render(request, 'registro/iniciar_sesion.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña es incorrecto'
            })
        else:
            login(request, usuario)
            return redirect('inicio')

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')