from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .models import Produto

def cadastrar_produto(request):
    if request.method =="GET":
        return render(request, 'cadastrar_produto.html')
    elif request.method == "POST":
        nome1 = request.POST.get('nome')
        preco1 = request.POST.get('preco')
        validade1 = request.POST.get('validade')
        quantidade1 = request.POST.get('quantidade')

        produto = Produto(
            nome=nome1,
            preco=preco1,
            validade=validade1,
            quantidade=quantidade1,
        )

        produto.save()

        return redirect('/estoque/cadastrar_produto')
    
def listar_produtos(request):
    produtos = Produto.objects.all()
    print(produtos)
    return render(request, 'listar_produtos.html', {'produtos': produtos})

def deletar_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect('/estoque/listar_produtos')
