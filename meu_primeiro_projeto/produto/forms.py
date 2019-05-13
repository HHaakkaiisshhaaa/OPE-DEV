from django.forms import ModelForm
from .models import Pessoa


class PessoaForm(ModelForm):
    class Meta:
        model  = Pessoa
        fields = ['primeiro_nome','ultimo_nome','idade','salario']