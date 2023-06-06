from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from BancoDeDados.models import SALAS
from .forms import SalaForm

@login_required()
def sala_list(request):
    salas = SALAS.objects.all()
    return render(request, 'sala.html', {'salas': salas})

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

    if form.is_valid():
        form.save()
        return redirect('sala_list')

    return render(request, 'salaForm.html', {'form': form})

@login_required()
def sala_delete(request, id):
    sala = get_object_or_404(SALAS, pk=id)
    form = SalaForm(request.POST or None, request.FILES or None, instance=sala)

    if request.method == 'POST':
        sala.delete()
        return redirect('sala_list')

    return render(request, 'salaDeleteConfirm.html', {'form': form})