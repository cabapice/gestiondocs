from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def cargos(request):
    return HttpResponse("<h1>Cargos</h1>")