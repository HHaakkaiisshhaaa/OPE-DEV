from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pessoa
from .forms import PessoaForm
from django.http import HttpResponse
 
@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas.html', {'pessoas' : pessoas})

@login_required
def new_pessoas(request):
    form = PessoaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_pessoas')
    return render(request, 'form.html', {'form': form})

@login_required
def update_pessoas(request, id):
    pessoas = get_object_or_404(Pessoa, pk = id)
    form = PessoaForm(request.POST or None, instance=pessoas)
    if form.is_valid():
        form.save()
        return redirect('lista_pessoas')
    return render(request, 'form.html', {'form':form})
    
@login_required
def delete_pessoas(request, id):
    pessoas = get_object_or_404(Pessoa, pk = id)
    form = PessoaForm(request.POST or None, instance=pessoas)

    if request.method == 'POST':
        pessoas.delete()
        return redirect('lista_pessoas')
    return render(request, 'pessoa_delete_confirme.html',{'form':form})