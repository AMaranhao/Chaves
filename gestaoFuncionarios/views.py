from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from BancoDeDados.models import FUNCIONARIO
from django.contrib.auth.models import User
from .forms import FuncionarioForm, UserForm, UserFormSemSenha
from django.db import transaction



@login_required
def funcionario_list(request):
    funcionarios = FUNCIONARIO.objects.all()
    return render(request, 'funcionario.html', {'funcionarios': funcionarios})

#TODO: ORGANIZAR UMA MANEIRA DE RECEBER TODOS OS DADOS DO FUNCIONARIO
@login_required
def funcionario_new(request):
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = FuncionarioForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            with transaction.atomic():
                userForm1 = form1.save()
                funcionarioForm2 = form2.save(commit=False)
                funcionarioForm2.User_FK = userForm1
                userForm1.save()
                funcionarioForm2.save()
            return redirect('funcionario_list')
    else:
        form1 = FuncionarioForm()
        form2 = UserForm()
    context = {
        'form1': form1,
        'form2': form2
    }

    return render(request, 'funcionarioForm.html', context)

#TODO: FINALIZAR O CRUD DE FUNCIONARIOS

@login_required
def funcionario_update(request, id):
    funcionario = get_object_or_404(FUNCIONARIO, pk=id)

    if request.method == 'POST':
        form1 = UserFormSemSenha(request.POST or None, request.FILES or None, instance=funcionario.User_FK)
        form2 = FuncionarioForm(request.POST, instance=funcionario)

        if form1.is_valid() and form2.is_valid():
            with transaction.atomic():
                user = form1.save()
                form2.save(commit=False)
                funcionario.User_FK = user
                funcionario.save()

            return redirect('funcionario_list')
    else:
        form1 = UserFormSemSenha(instance=funcionario.User_FK)
        form2 = FuncionarioForm(instance=funcionario)

    context = {
        'form1': form1,
        'form2': form2
    }
#    return render(request, 'funcionarioForm.html', context)
    return render(request, 'funcionarioFormUpdate.html', context)
#TODO: Fazer uma view para mudanca de senha
"""
@login_required
def change_password(request, id):
    funcionario = get_object_or_404(FUNCIONARIO, pk=id)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('funcionario_list')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'change_password.html', {'form': form})
"""

@login_required
def funcionario_delete(request, id):
    funcionario = get_object_or_404(FUNCIONARIO, pk=id)
    form = FuncionarioForm(request.POST or None, request.FILES or None, instance=funcionario)

    if request.method == 'POST':
        funcionario.delete()
        return redirect('funcionario_list')

    return render(request, 'funcionarioDeleteConfirm.html', {'form': form})


