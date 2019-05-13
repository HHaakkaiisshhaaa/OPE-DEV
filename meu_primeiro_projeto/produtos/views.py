from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto
from .forms import ProdutoForm
from django.http import HttpResponse
 

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def lista_produto(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos' : produtos})

@login_required
def novo_produto(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_produto')
    return render(request, 'form.html', {'form': form})

@login_required
def update_produto(request, id):
    produtos = get_object_or_404(Produto, pk = id)
    form = ProdutoForm(request.POST or None, instance=produtos)
    if form.is_valid():
        form.save()
        return redirect('lista_produto')
    return render(request, 'form.html', {'form':form})
    
@login_required
def delete_produto(request, id):
    produtos = get_object_or_404(Produto, pk = id)
    form = ProdutoForm(request.POST or None, instance=produtos)

    if request.method == 'POST':
        produtos.delete()
        return redirect('lista_produto')
    return render(request, 'produto_delete_confirme.html',{'form':form})