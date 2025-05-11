from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.


# estoque\urls.py - index.html
def index(request):
    return render(request, 'index.html')

def listarItens(request):

    itens = Item.objects.all()

    return render(request,  "itens.html", {"itens":itens})