from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def empresas(request):
    return HttpResponse("<h1>Empresas</h1>")
