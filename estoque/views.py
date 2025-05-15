from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Item, Estoque

# Create your views here.


# estoque\urls.py - index.html
def index(request):
    return render(request, 'index.html')

def listarItens(request):

    estoque = Estoque.objects.all()

    return render(request,  "itens.html", {"estoque":estoque})

def saidaItem(request, id):   

        estoque = Estoque.objects.get(id=id)
        if request.method == 'POST':
            quantidade_out = int(request.POST.get('quantidade'))
            estoque.quantidade -= quantidade_out
            estoque.save()
            return HttpResponseRedirect('/api/estoque/itens')

        return render(request, 'saidaItem.html', {'estoque': estoque})


def entradaItem(request, id):
        estoque = Estoque.objects.get(id=id)
        if request.method == 'POST':
            quantidade_add = int(request.POST.get('quantidade'))
            estoque.quantidade += quantidade_add
            estoque.save()
            return HttpResponseRedirect('/api/estoque/itens')

        return render(request, 'entradaItem.html', {'estoque': estoque})

def novoEstoque(request):
    if(request.method == "POST"):
         quantidade = request.POST.get('quantidade')
         endereco = request.POST.get('endereco')
         item = Item.objects.get(id=request.POST.get('item'))

         novo_estoque = Estoque(quantidade = quantidade,
                                endereco = endereco,
                                item = item)
         novo_estoque.save()
         return HttpResponseRedirect('/api/estoque/itens')
    
    itens = Item.objects.all()
    return render(request,"novoEstoque.html",{'itens':itens})

def editarEstoque(request, id):
    if request.method == "POST":
        quantidade = request.POST.get('quantidade')
        endereco = request.POST.get('endereco')
        item = Item.objects.get(id=request.POST.get('item'))

        editar_estoque = Estoque.objects.get(id=id)
        editar_estoque.quantidade = quantidade
        editar_estoque.endereco = endereco
        editar_estoque.item = item
        editar_estoque.save()

        return HttpResponseRedirect('/api/estoque/itens')
    else:
        estoque = Estoque.objects.get(id=id)
        itens = Item.objects.all()

    return render(request,"novoEstoque.html",{'estoque' : estoque, 'itens' : itens})


def excluirEstoque(request,id):
    estoque = Estoque.objects.get(id=id)
    estoque.delete()
    return HttpResponseRedirect('/api/estoque/itens')