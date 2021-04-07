from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import DocForm
from .forms import UploadDocForm
from .forms import PastaForm
from django.contrib import messages

from .models import Documento 
from .models import EDocModel
from .models import Pasta

@login_required
def pastaList(request):
    pastas_list = Pasta.objects.all().order_by('-created_at')

    paginator = Paginator(pastas_list, 4)

    page = request.GET.get('page')

    pastas = paginator.get_page(page)

    return render(request, 'documentos/home.html', {'pastas': pastas})

@login_required
def pastaView(request, id):
    pasta = get_object_or_404(Pasta, pk=id)
    return render(request, 'documentos/pasta.html', {'pasta': pasta})

@login_required
def novaPasta(request):
    if request.method == 'POST':
        form = PastaForm(request.POST)
        if form.is_valid():
            pasta = form.save(commit=False)
            pasta.save()
            return redirect('/')

    else:    
        form = PastaForm()
        return render(request,'documentos/novapasta.html', {'form': form})

@login_required
def deletePasta(request, id):
    pasta = get_object_or_404(Pasta, pk=id)
    pasta.delete()
    return redirect('/')

@login_required
def itensList(request, id):
    itens_list = EDocModel.objects.all()#.order_by('-created_at')

    paginator = Paginator(itens_list, 4)

    page = request.GET.get('page')

    itens = paginator.get_page(page)

    return render(request, 'documentos/itenslist.html', {'itens': itens})


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
    form = UploadDocForm
    if request.method == 'POST':
        form = UploadDocForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    return render(request, 'documentos/upload.html', {'form': form})
    

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

