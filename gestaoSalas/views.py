from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from BancoDeDados.models import SALAS, FUNCIONARIO
from .forms import SalaForm

@login_required()
def sala_list(request):
    salas = SALAS.objects.all()
    usuarioLogado = FUNCIONARIO.objects.get(User_FK=request.user)

    context = {
        'salas': salas,
        'usuarioLogado': usuarioLogado,
    }

    return render(request, 'sala.html', context)

@login_required()
def sala_new(request):
    form = SalaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('sala_list')
    return render(request, 'salaForm.html', {'form': form})

@login_required()
def sala_update(request, id):
    sala = get_object_or_404(SALAS, pk=id)
    form = SalaForm(request.POST or None, request.FILES or None, instance=sala)
    usuarioLogado = FUNCIONARIO.objects.get(User_FK=request.user)

    if form.is_valid():
        form.save()
        return redirect('sala_list')

    context = {
        'form': form,
        'usuarioLogado': usuarioLogado,
    }

    return render(request, 'salaForm.html', context)

@login_required()
def sala_delete(request, id):
    sala = get_object_or_404(SALAS, pk=id)
    form = SalaForm(request.POST or None, request.FILES or None, instance=sala)

    if request.method == 'POST':
        sala.delete()
        return redirect('sala_list')

    return render(request, 'salaDeleteConfirm.html', {'form': form})