from django import forms
from django.forms import ModelForm
from BancoDeDados.models import FUNCIONARIO
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core.exceptions import ValidationError
from django.db import transaction

class FuncionarioForm(ModelForm):
    class Meta:
        model = FUNCIONARIO
        fields = ['CPF', 'Matricula', 'Telefone', 'Curso_FK', 'Cargo_FK']
        labels = {
            'Curso_FK': 'Curso',
            'Cargo_FK': 'Cargo',
        }

        def clean_CPF(self):
            cpf = self.cleaned_data['CPF']
            if User.objects.filter(CPF=cpf).exists():
                raise forms.ValidationError('Este CPF já está em uso.')
            return cpf


        def clean_Matricula(self):
            matricula = self.cleaned_data['Matricula']
            if User.objects.filter(Matricula=matricula).exists():
                raise forms.ValidationError('Esta Matricula já está em uso.')
            return matricula


class FuncionarioFormUpdate(ModelForm):
    class Meta:
        model = FUNCIONARIO
        fields = ['Telefone', 'Curso_FK', 'Cargo_FK']
        labels = {
            'Curso_FK': 'Curso',
            'Cargo_FK': 'Cargo',
        }


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        max_length=150,
        help_text=None
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        labels = {
            'username': 'Usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'Email Senac'
        }
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError("As senhas não coincidem.")
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
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        max_length=150,
        help_text=None
    )
#TODO:Autoinserir o @fac.pe.senac.br no campo email
    email = forms.EmailField(
        help_text='@fac.pe.senac.br',
        required=True
    )
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'username': 'Usuário',
            'email': 'Email Senac',
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
    is_active = forms.NullBooleanField(
        widget=forms.CheckboxInput)
    class Meta:
        model = User
        fields = ['is_active']

    def __init__(self, *args, **kwargs):
        super(UserFormInativo, self).__init__(*args, **kwargs)
        self.fields['is_active'].label = 'Está Ativo'