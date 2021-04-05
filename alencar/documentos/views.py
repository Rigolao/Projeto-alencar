from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import DocForm
from django.contrib import messages

from .models import Documento

@login_required
def empresaHome(request):
    return render(request, 'documentos/home.html')

@login_required
def empresaDoc(request):

    search = request.GET.get('search')
    filter = request.GET.get('filter')

    if search:

        documentos = Documento.objects.filter(title__icontains=search, user=request.user)

    elif filter:

        documentos = Documento.objects.filter(tipo=filter, user=request.user)

    else:

        documentos_list = Documento.objects.all().order_by('-created_at').filter(user=request.user)

        paginator = Paginator(documentos_list, 5)

        page = request.GET.get('page')

        documentos = paginator.get_page(page)

    return render(request, 'documentos/doc.html', {'documentos': documentos})

@login_required
def documentoView(request, id):
    documento = get_object_or_404(Documento, pk=id)
    return render(request, 'documentos/documento.html', {'documento': documento})

@login_required
def novoDoc(request):
    if request.method == 'POST':
        form = DocForm(request.POST)

        if form.is_valid():
            documento = form.save(commit=False)
            documento.user = request.user
            documento.save()
            messages.info(request, 'Documento adicionado com sucesso')
            return redirect('/doc')

    else:
        form = DocForm()
        return render(request, 'documentos/novodoc.html', {'form': form})

@login_required
def editDoc(request, id):
    documento = get_object_or_404(Documento, pk=id)
    form = DocForm(instance=documento)

    if(request.method == 'POST'):
        form = DocForm(request.POST, instance=documento)

        if(form.is_valid()):
            documento.save()
            messages.info(request, 'Documento alterado com sucesso')
            return redirect('/doc')
        else:
            return render(request, 'documentos/editdoc.html', {'form': form, 'documento': documento})
    else:
        return render(request, 'documentos/editdoc.html', {'form': form, 'documento': documento})

@login_required
def deleteDoc(request, id):
        documento = get_object_or_404(Documento, pk=id)
        documento.delete()

        messages.info(request, 'Documento deletado com sucesso')

        return redirect('/doc')