from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Documento

def empresaHome(request):
    return render(request, 'documentos/home.html')

def empresaDoc(request):
    documentos = Documento.objects.all()
    return render(request, 'documentos/doc.html', {'documentos': documentos})

def documentoView(request, id):
    documento = get_object_or_404(Documento, pk=id)
    return render(request, 'documentos/documento.html', {'documento': documento})