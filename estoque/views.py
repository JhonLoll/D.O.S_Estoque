from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from .models import Estoque

# API Views
from rest_framework import viewsets, permissions
from .serializers import EstoqueSerializer

API_PRODUTOS_URL = 'https://aramesinho.pythonanywhere.com/api/produtos/'


class EstoqueViewSet(viewsets.ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer
    permission_classes = [permissions.AllowAny]

# estoque\urls.py - index.html
def index(request):
    return render(request, 'index.html')

def listarItens(request):
    estoque_local = Estoque.objects.all()
    itens_api_list = []
    try:
        response = requests.get(API_PRODUTOS_URL)
        print("--- Resposta da API (primeiros 500 caracteres) ---")
        print(response.text[:500]) # Mostra o início da resposta da API
        response.raise_for_status() # Lança exceção para códigos de erro HTTP (4xx ou 5xx)
        itens_api_list = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar itens da API: {e}")
        
    # Mapeia os IDs dos itens da API para fácil acesso
    itens_api_map = {item_api['id']: item_api for item_api in itens_api_list}
    print("\n--- IDs disponíveis na API (Chaves do Mapa) ---")
    for api_id_key in itens_api_map.keys():
        print(f"API ID Key: '{api_id_key}' (Tipo: {type(api_id_key)})")

    estoque_com_info = []
    print("\n--- Comparando Estoque Local com IDs da API ---")
    for est_obj in estoque_local:
        item_info = None
        local_id_item_str = None
        if est_obj.id_item: 
            local_id_item_str = str(est_obj.id_item) # Garante que é uma string
            item_info = itens_api_map.get(local_id_item_str)
            print(f"Estoque Local ID: {est_obj.id}, id_item: '{local_id_item_str}' (Tipo: {type(local_id_item_str)})")
            if item_info:
                print(f"  -> Encontrado na API: Sim. Nome do item: {item_info.get('nome')}")
            else:
                print(f"  -> Encontrado na API: Não. '{local_id_item_str}' não corresponde a nenhuma chave no mapa da API.")
        else:
            print(f"Estoque Local ID: {est_obj.id}, id_item é None.")
        estoque_com_info.append({
            'estoque': est_obj,
            'item_info': item_info
        })
    return render(request,  "itens.html", {"estoque_data": estoque_com_info})

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
        id_item_selecionado = request.POST.get('id_item') # ID do item da API externa

        novo_estoque = Estoque(quantidade=quantidade,
                               endereco=endereco,
                               id_item=id_item_selecionado if id_item_selecionado else None)
        novo_estoque.save()
        return HttpResponseRedirect('/api/estoque/itens')
    
    itens_api = []
    try:
        response = requests.get(API_PRODUTOS_URL)
        response.raise_for_status()
        itens_api = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar itens da API para novoEstoque: {e}")
        # Tratar erro, talvez passar mensagem para o template

    return render(request,"novoEstoque.html",{'itens_api': itens_api})

def editarEstoque(request, id):
    estoque_obj = Estoque.objects.get(id=id)
    if request.method == "POST":
        quantidade = request.POST.get('quantidade')
        endereco = request.POST.get('endereco')
        id_item_selecionado = request.POST.get('id_item') # ID do item da API externa

        estoque_obj.quantidade = quantidade
        estoque_obj.endereco = endereco
        estoque_obj.id_item = id_item_selecionado if id_item_selecionado else None
        estoque_obj.save()

        return HttpResponseRedirect('/api/estoque/itens')
    else:
        itens_api = []
        try:
            response = requests.get(API_PRODUTOS_URL)
            response.raise_for_status()
            itens_api = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar itens da API para editarEstoque: {e}")
            # Tratar erro

    return render(request,"novoEstoque.html",{'estoque' : estoque_obj, 'itens_api' : itens_api})


def excluirEstoque(request,id):
    estoque = Estoque.objects.get(id=id)
    estoque.delete()
    return HttpResponseRedirect('/api/estoque/itens')
    
def listarCadastrarItem(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao', '')
        preco = request.POST.get('preco')
        marca = request.POST.get('marca')

        # O JSON da API externa para item é: { "nome": "", "descricao": "", "preco": null, "saldo_estoque": null, "marca": "" }
        # Não enviaremos saldo_estoque na criação.
        payload = {
            "nome": nome,
            "descricao": descricao,
            "preco": preco if preco else None, # Envia null se preço for vazio/None
            "marca": marca
        }
        try:
            response = requests.post(API_PRODUTOS_URL, json=payload)
            response.raise_for_status()
            # Item criado com sucesso na API externa
        except requests.exceptions.RequestException as e:
            print(f"Erro ao cadastrar item na API: {e}")
            if response is not None:
                print(f"Detalhes do erro da API: {response.text}")
            # Adicionar tratamento de erro, e.g., mensagem para o usuário
            # return render(request, "gerenciar_itens.html", {"error_message": "Falha ao cadastrar item.", "itens": []}) # Exemplo
        return HttpResponseRedirect('/api/estoque/gerenciar-itens')
    
    itens = []
    try:
        response = requests.get(API_PRODUTOS_URL)
        response.raise_for_status() # Lança exceção para códigos de erro HTTP (4xx ou 5xx)
        itens = response.json() 
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar itens: {e}")
    return render(request, "gerenciar_itens.html", {"itens": itens}) # Alterado para gerenciar_itens.html

def excluirItem(request, item_id): # item_id é o ID do item da API externa (string UUID)
    try:
        # A API pode esperar um trailing slash: {API_PRODUTOS_URL}{item_id}/
        delete_url = f"{API_PRODUTOS_URL}{item_id}/" 
        response = requests.delete(delete_url)
        response.raise_for_status() # Lança exceção para erros HTTP
        # Item excluído com sucesso na API externa
    except requests.exceptions.RequestException as e:
        print(f"Erro ao excluir item na API: {e}")
        if response is not None:
            print(f"Detalhes do erro da API: {response.text}")
        # Adicionar tratamento de erro, e.g., mensagem para o usuário
    return HttpResponseRedirect('/api/estoque/gerenciar-itens')