from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sedes(request):
    return HttpResponse("<h1>Sedes</h1>")