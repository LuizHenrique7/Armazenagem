from django.shortcuts import render

from .models import Produto


def home(request):
    if request.method == 'POST':
        produto = Produto()
        produto.nome = request.POST.get("nome_produto")
        produto.imagemURL = request.POST.get("imagem")
        produto.preco_unitario = request.POST.get("preco_unitario")
        if request.POST.get("ativo") == 'on':
            produto.ativo = True
            print(produto.ativo)
        else:
            produto.ativo = False
        produto.quantidade_estoque = request.POST.get("quantidade_estoque")
        produto.save()

    return render(request, 'home.html')


def produto(request):
    lista_produto = Produto.objects.all()

    return render(request, 'produto.html', {'lista_produto': lista_produto})


def buscar_produto(request):
    lista = Produto.objects.all()
    busca = request.GET.get('search')

    if busca:
        lista = Produto.objects.filter(nome__icontains=busca)

    return render(request, 'index.html', {'lista': lista})
