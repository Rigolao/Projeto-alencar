from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import DocForm
from .forms import UploadDocForm
from django.contrib import messages

from .models import Documento 
from .models import EDocModel

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
def DocUploadView(request):
    if request.method == 'POST':
        form = UploadDocForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/doc')
    else:
        form = UploadDocForm()
        context = {'form', form}
        return render(request, 'documentos/upload.html', context)
    

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