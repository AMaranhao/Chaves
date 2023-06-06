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

        def clean_username(self):
            cpf = self.cleaned_data['CPF']
            if User.objects.filter(CPF=cpf).exists():
                raise forms.ValidationError('Este CPF já está em uso.')
            return cpf

        def clean_email(self):
            matricula = self.cleaned_data['Matricula']
            if User.objects.filter(Matricula=matricula).exists():
                raise forms.ValidationError('Esta Matricula já está em uso.')
            return matricula


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        max_length=150,
        help_text=None
    )
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

        def clean_username(self):
            username = self.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError('Este nome de usuário já está em uso.')
            return username

        def clean_email(self):
            email = self.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Este email já está em uso.')
            return email

class UserFormUpdate(ModelForm):
    is_active = forms.NullBooleanField(widget=forms.NullBooleanSelect)
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        max_length=150,
        help_text=None
    )
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active']
        labels = {
            'username': 'Usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'Email Senac',
            'is_active':'Ativo'
        }

        def clean_username(self):
            username = self.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError('Este nome de usuário já está em uso.')
            return username

        def clean_email(self):
            email = self.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Este email já está em uso.')
            return email

class UserFormInativo(ModelForm):
    class Meta:
        model = User
        fields = ['is_active']
        labels = {
            'username': 'Usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'Email Senac'
        }