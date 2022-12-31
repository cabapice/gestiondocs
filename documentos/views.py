from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Documento
from .forms import DocumentoForm

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def documentos(request):
    documentos = Documento.objects.all()      
    return render(request, 'documento/index.html', {'documentos': documentos})
def crear_doc(request):
    formulario = DocumentoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('documentos')
    return render(request, 'documento/crear.html', {'formulario': formulario})

def editar_doc(request, id_doc):
    documento = Documento.objects.get(id_doc=id_doc)
    formulario = DocumentoForm(request.POST or None, request.FILES or None, instance=documento)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('documentos')
    return render(request, 'documento/editar.html', {'formulario': formulario})
def eliminar_doc(request, id_doc):
    documento = Documento.objects.get(id_doc=id_doc)
    documento.delete()
    return redirect('documentos')