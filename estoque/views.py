from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Item

# Create your views here.


# estoque\urls.py - index.html
def index(request):
    return render(request, 'index.html')

def listarItens(request):

    itens = Item.objects.all()

    return render(request,  "itens.html", {"itens":itens})

def saidaItem(request, id):   

        item = Item.objects.get(id=id)
        if request.method == 'POST':
            quantidade_out = int(request.POST.get('quantidade'))
            item.quantidade -= quantidade_out
            item.save()
            return HttpResponseRedirect('/api/estoque/itens')

        return render(request, 'saidaItem.html', {'item': item})


def entradaItem(request, id):
        item = Item.objects.get(id=id)
        if request.method == 'POST':
            quantidade_add = int(request.POST.get('quantidade'))
            item.quantidade += quantidade_add
            item.save()
            return HttpResponseRedirect('/api/estoque/itens')

        return render(request, 'entradaItem.html', {'item': item})

def cadastroItem(request):
    return

def editarItem(request):
    return

def excluirItem(request):
    return