from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm
from django.http import HttpResponse

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas.html', {'pessoas' : pessoas})


def new_pessoas(request):
    form = PessoaForm(request.POST, None)

    if form.is_valid():
        form.save()
        return redirect('lista_pessoas')
    return render(request, 'form.html', {'form': form})
