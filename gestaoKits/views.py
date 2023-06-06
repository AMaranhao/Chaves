from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from BancoDeDados.models import KITS
from .forms import KitForm

@login_required()
def kit_list(request):
    kits = KITS.objects.all()
    return render(request, 'kit.html', {'kits': kits})

@login_required()
def kit_new(request):
    form = KitForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('kit_list')
    return render(request, 'kitForm.html', {'form': form})

@login_required()
def kit_update(request, id):
    kit = get_object_or_404(KITS, pk=id)
    form = KitForm(request.POST or None, request.FILES or None, instance=kit)

    if form.is_valid():
        form.save()
        return redirect('kit_list')

    return render(request, 'kitForm.html', {'form': form})

@login_required()
def kit_delete(request, id):
    kit = get_object_or_404(KITS, pk=id)
    form = KitForm(request.POST or None, request.FILES or None, instance=kit)

    if request.method == 'POST':
        kit.delete()
        return redirect('kit_list')

    return render(request, 'kitDeleteConfirm.html', {'form': form})