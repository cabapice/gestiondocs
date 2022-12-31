from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def areas(request):
    return HttpResponse("<h1>Areas</h1>")
