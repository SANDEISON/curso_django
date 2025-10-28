# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm


def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/list.html', {'produtos': produtos})


def produto_create(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/form.html', {'form': form})


def produto_update(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/form.html', {'form': form})


def produto_delete(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        produto.delete()
        return redirect('produto_list')
    return render(request, 'produtos/delete.html', {'produto': produto})
