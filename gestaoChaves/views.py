from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from BancoDeDados.models import CHAVES
from .forms import ChaveForm

@login_required()
def chave_list(request):
    chaves = CHAVES.objects.all()
    return render(request, 'chave.html', {'chaves': chaves})

@login_required()
def chave_new(request):
    form = ChaveForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('chave_list')
    return render(request, 'chaveForm.html', {'form': form})

@login_required()
def chave_update(request, id):
    chave = get_object_or_404(CHAVES, pk=id)
    form = ChaveForm(request.POST or None, instance=chave)

    if form.is_valid():
        form.save()
        return redirect('chave_list')

    return render(request, 'chaveForm.html', {'form': form})

@login_required()
def chave_delete(request, id):
    chave = get_object_or_404(CHAVES, pk=id)
    form = ChaveForm(request.POST or None, instance=chave)

    if request.method == 'POST':
        chave.delete()
        return redirect('chave_list')

    return render(request, 'chaveDeleteConfirm.html', {'form': form})