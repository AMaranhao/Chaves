from django import forms
from django.forms import ModelForm
from BancoDeDados.models import FUNCIONARIO
from django.contrib.auth.models import User


class FuncionarioForm(ModelForm):
    class Meta:
        model = FUNCIONARIO
        fields = ['CPF', 'Matricula', 'Telefone', 'Curso_FK', 'Cargo_FK']
        labels = {
            'Curso_FK': 'Curso',
            'Cargo_FK': 'Cargo',
        }


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['password', 'username', 'first_name', 'last_name', 'email']
        labels = {
            'password': 'Senha',
            'username': 'Usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'Email Senac'
        }

class UserFormSemSenha(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'Email Senac'
        }