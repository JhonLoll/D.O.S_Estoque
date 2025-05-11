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

def saidaItens(request, id):   

        item = Item.objects.get(id=id)
        if request.method == 'POST':
            quantidade_retirada = int(request.POST.get('quantidade'))
            item.quantidade -= quantidade_retirada
            item.save()
            return HttpResponseRedirect('/api/estoque/itens')

        return render(request, 'saidaItem.html', {'item': item})


def entradaItem(request):
    return

def cadastroItem(request):
    return

def editarItem(request):
    return

def excluirItem(request):
    return