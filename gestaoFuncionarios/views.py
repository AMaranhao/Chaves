from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.decorators import login_required
from BancoDeDados.models import FUNCIONARIO
from django.contrib.auth.models import User
from .forms import FuncionarioForm, UserForm, UserFormUpdate
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core.exceptions import ValidationError




@login_required
def funcionario_list(request):
    funcionarios = FUNCIONARIO.objects.all()
    return render(request, 'funcionario.html', {'funcionarios': funcionarios})


@login_required
def funcionario_new(request):
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = FuncionarioForm(request.POST)
        context = {
            'form1': form1,
            'form2': form2
        }
        if form1.is_valid() and form2.is_valid():
            with transaction.atomic():
                userForm1 = form1.save(commit=False)
                password = form1.cleaned_data['password']
                try:
                    validate_password(password, user=userForm1)
                except ValidationError as e:
                    form1.add_error('password', e)
                    return render(request, 'funcionarioForm.html', context)

                userForm1.set_password(password)
                userForm1.save()

                funcionarioForm2 = form2.save(commit=False)
                funcionarioForm2.User_FK = userForm1
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


@login_required
def funcionario_update(request, id):
    funcionario = get_object_or_404(FUNCIONARIO, pk=id)

    if request.method == 'POST':
        form1 = UserFormUpdate(request.POST or None, request.FILES or None, instance=funcionario.User_FK)
        form2 = FuncionarioForm(request.POST, instance=funcionario)

        if form1.is_valid() and form2.is_valid():
            with transaction.atomic():
                user = form1.save()
                form2.save(commit=False)
                funcionario.User_FK = user
                funcionario.save()

            return redirect('funcionario_list')
    else:
        form1 = UserFormUpdate(instance=funcionario.User_FK)
        form2 = FuncionarioForm(instance=funcionario)

    context = {
        'form1': form1,
        'form2': form2
    }
#    return render(request, 'funcionarioForm.html', context)
    return render(request, 'funcionarioFormUpdate.html', context)

"""
@login_required
def set_password(request, id):
    funcionario = get_object_or_404(FUNCIONARIO, pk=id)
    user = funcionario.USER_FK

    if request.method == 'POST':
        form = SetPasswordForm(user=user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('funcionario_list')
    else:
        form = SetPasswordForm(user=user)
    context = {
        'form': form,
    }

    return render(request, 'changePassword.html', context)
"""

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

    return render(request, 'changePassword.html', {'form': form})

"""
@login_required
def change_password(request, id):
    funcionario = get_object_or_404(FUNCIONARIO, pk=id)
    user = funcionario.USER_FK

    if request.method == 'POST':
        form = SetPasswordForm(user=user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('funcionario_list')
    else:
        form = SetPasswordForm(user=user)
    context = {
        'form': form,
    }

    return render(request, 'changePassword.html', extra_context=context, post_change_redirect='funcionario_list')

@login_required
def change_password_success(request):
    return render(request, 'changePasswordSuccess.html')


@login_required
def funcionario_delete(request, id):
    funcionario = get_object_or_404(FUNCIONARIO, pk=id)
    form = FuncionarioForm(request.POST or None, request.FILES or None, instance=funcionario)

    if request.method == 'POST':
        user = funcionario.User_FK
        funcionario.delete()
        user.delete()
        return redirect('funcionario_list')
    context = {
        'form': form,
    }

    return render(request, 'funcionarioDeleteConfirm.html', context)





