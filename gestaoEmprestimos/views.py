from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from BancoDeDados.models import EMPRESTIMOS, FUNCIONARIO
from .forms import EmprestimoForm

@login_required()
def emprestimo_list(request):
    emprestimos = EMPRESTIMOS.objects.all()
    usuarioLogado = FUNCIONARIO.objects.get(User_FK=request.user)

    context = {
        'emprestimos': emprestimos,
        'usuarioLogado': usuarioLogado,
    }

    return render(request, 'emprestimo.html', context)

@login_required()
def emprestimo_new(request):
    form = EmprestimoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('emprestimo_list')

    context = {
        'form': form
    }

    return render(request, 'emprestimoForm.html', context)

@login_required()
def emprestimo_update(request, id):
    emprestimo = get_object_or_404(EMPRESTIMOS, pk=id)
    form = EmprestimoForm(request.POST or None, request.FILES or None, instance=emprestimo)
    usuarioLogado = FUNCIONARIO.objects.get(User_FK=request.user)

    if form.is_valid():
        form.save()
        return redirect('emprestimo_list')

    context = {
        'form': form,
        'usuarioLogado': usuarioLogado,
    }

    return render(request, 'emprestimoForm.html', context)

@login_required()
def emprestimo_delete(request, id):
    emprestimo = get_object_or_404(EMPRESTIMOS, pk=id)
    form = EmprestimoForm(request.POST or None, request.FILES or None, instance=emprestimo)

    if request.method == 'POST':
        emprestimo.delete()
        return redirect('emprestimo_list')

    context = {
        'form': form
    }

    return render(request, 'emprestimoDeleteConfirm.html', context)