from django.shortcuts import render
from django.http import HttpResponse




def hello(request):
    return render(request, 'index.html')


def articles(request, year):
    return HttpResponse('O ano digitado é'+ str(year))


def lerDoBanco(nome):
    lista_nomes = [
        {'nome': 'Andrei', 'Idade': 0},
        {'nome': 'Elizete', 'Idade': 26},
        {'nome': 'Andrew', 'Idade': 1},
        ]
    for pessoa in lista_nomes:
        if pessoax['nome'] == nome:
            return pessoax
    else: 
        return {'nome': 'não encontrado', 'idade': 0}

def fname(request, nome):
    result = lerDoBanco(nome)
    if result['Idade'] > 0:
        return HttpResponse('A {} possui {} anos de idade'.format(result['nome'], result['Idade']))
    else:
        return HttpResponse('A pessoa não foi encontrada')


def fname2(request, nome):
    idade= lerDoBanco(nome)['Idade']
    return render(request, 'pessoas.html', {'v_idade': idade})


