from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..BancoDeDados.models import AGENDAMENTO, FUNCIONARIO
from .forms import AgendamentoForm
from ..gestaoEmprestimos.forms import EmprestimoForm, CursoEmprestimoForm

@login_required()
def agendamento_list(request):
    agendamentos = AGENDAMENTO.objects.all()
    funcionario_logado = FUNCIONARIO.objects.get(User_FK=request.user)

    context = {
        'agendamentos':agendamentos
        ,'funcionario_logado': funcionario_logado
    }
    return render(request, 'agendamento.html', context)

@login_required()
def agendamento_new(request):
    form = AgendamentoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('agendamento_list')

    current_user = request.user
    funcionarios = FUNCIONARIO.objects.filter(Curso_FK=current_user.funcionario.Curso_FK)

    form.fields['Funcionario_FK'].queryset = funcionarios
    funcionario_logado = FUNCIONARIO.objects.get(User_FK=request.user)
    context = {
        'form': form,
        'funcionario_logado': funcionario_logado
    }

    return render(request, 'agendamentoForm.html', context)

@login_required()
def agendamento_update(request, id):
    agendamento = get_object_or_404(AGENDAMENTO, pk=id)
    funcionario_logado = FUNCIONARIO.objects.get(User_FK=request.user)

    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento, usuario_logado=funcionario_logado)
        if form.is_valid():
            form.save()
            return redirect('agendamento_list')
    else:
        form = AgendamentoForm(instance=agendamento, usuario_logado=funcionario_logado)

    context = {
        'form': form,
        'funcionario_logado': funcionario_logado,
        'agendamento': agendamento
    }
    return render(request, 'agendamentoForm.html', context)
'''
def agendamento_update(request, id):
    agendamento = get_object_or_404(AGENDAMENTO, pk=id)
    funcionario_logado = FUNCIONARIO.objects.get(User_FK=request.user)

    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento, usuario_logado=funcionario_logado)
        if form.is_valid():
            form.save()
            return redirect('agendamento_list')
    else:
        form = AgendamentoForm(instance=agendamento, usuario_logado=funcionario_logado)

    funcionarios = FUNCIONARIO.objects.all()
    #current_user = request.user
    #funcionarios = FUNCIONARIO.objects.filter(Curso_FK=current_user.funcionario.Curso_FK)

    form.fields['Funcionario_FK'].queryset = funcionarios

    context = {
        'form': form
        ,'funcionario_logado': funcionario_logado
        ,'agendamento': agendamento
    }
    return render(request, 'agendamentoForm.html', context)

'''






@login_required()
def agendamento_delete(request, id):
    agendamento = get_object_or_404(AGENDAMENTO, pk=id)
    form = AgendamentoForm(request.POST or None, request.FILES or None, instance=agendamento)

    if request.method == 'POST':
        agendamento.delete()
        return redirect('agendamento_list')

    return render(request, 'agendamentoDeleteConfirm.html', {'form': form})


@login_required()
def agendamento_emprestimo(request):
    form1 = CursoEmprestimoForm(request.POST or None, request.FILES or None)
    form2 = EmprestimoForm(request.POST or None, request.FILES or None, curso_fk=form1['Curso_FK'].value())
    funcionario_logado = FUNCIONARIO.objects.get(User_FK=request.user)

    if form2.is_valid():
        form2.save()
        return redirect('agendamento_list')

    context = {
        'form1': form1
        ,'form2': form2
        , 'funcionario_logado': funcionario_logado
    }

    return render(request, 'agendamentoEmprestimo.html', context)

