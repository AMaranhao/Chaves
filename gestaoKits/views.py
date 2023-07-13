from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from BancoDeDados.models import KITS, FUNCIONARIO
from .forms import KitForm

@login_required()
def kit_list(request):
    kits = KITS.objects.all()
    usuarioLogado = FUNCIONARIO.objects.get(User_FK=request.user)

    context = {
        'kits': kits,
        'usuarioLogado': usuarioLogado,
    }

    return render(request, 'kit.html', context)

@login_required()
def kit_new(request):
    form = KitForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('kit_list')

    context = {
        'form': form
    }

    return render(request, 'kitForm.html', context)

@login_required()
def kit_update(request, id):
    kit = get_object_or_404(KITS, pk=id)
    form = KitForm(request.POST or None, request.FILES or None, instance=kit)
    usuarioLogado = FUNCIONARIO.objects.get(User_FK=request.user)

    if form.is_valid():
        form.save()
        return redirect('kit_list')

    context = {
        'form': form,
        'usuarioLogado': usuarioLogado,
    }

    return render(request, 'kitForm.html', context)

@login_required()
def kit_delete(request, id):
    kit = get_object_or_404(KITS, pk=id)
    form = KitForm(request.POST or None, request.FILES or None, instance=kit)

    if request.method == 'POST':
        kit.delete()
        return redirect('kit_list')

    context = {
        'form': form
    }

    return render(request, 'kitDeleteConfirm.html', context)