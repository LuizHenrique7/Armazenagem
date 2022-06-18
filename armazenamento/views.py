from django.shortcuts import render

from .models import Produto


def home(request):
    lista = Produto.objects.all()
    busca = request.GET.get('search')
    if busca:
        lista = Produto.objects.filter(nome__icontains=busca)

    if request.method == 'POST':
        produto = Produto()
        produto.nome = request.POST.get("nome_produto")
        produto.imagemURL = request.POST.get("imagem")
        produto.preco_unitario = request.POST.get("preco_unitario")
        if request.POST.get("ativo") == 'on':
            produto.ativo = True
        else:
            produto.ativo = False
        produto.quantidade_estoque = request.POST.get("quantidade_estoque")
        produto.save()

    return render(request, 'home.html', {'lista': lista})
