from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from BancoDeDados.models import AGENDAMENTO
from .forms import AgendamentoForm

@login_required()
def agendamento_list(request):
    agendamentos = AGENDAMENTO.objects.all()
    return render(request, 'agendamento.html', {'agendamentos': agendamentos})

@login_required()
def agendamento_new(request):
    form = AgendamentoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('agendamento_list')
    return render(request, 'agendamentoForm.html', {'form': form})

@login_required()
def agendamento_update(request, id):
    agendamento = get_object_or_404(AGENDAMENTO, pk=id)
    form = AgendamentoForm(request.POST or None, request.FILES or None, instance=agendamento)

    if form.is_valid():
        form.save()
        return redirect('agendamento_list')

    return render(request, 'agendamentoForm.html', {'form': form})

@login_required()
def agendamento_delete(request, id):
    agendamento = get_object_or_404(AGENDAMENTO, pk=id)
    form = AgendamentoForm(request.POST or None, request.FILES or None, instance=agendamento)

    if request.method == 'POST':
        agendamento.delete()
        return redirect('agendamento_list')

    return render(request, 'agendamentoDeleteConfirm.html', {'form': form})