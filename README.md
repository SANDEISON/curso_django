# 📘Curso de Django (Python)

## 🔹 Aula 10 – Views Baseadas em Função (FBV)

As Function Based Views são formas de construir views no Django utilizando funções Python comuns.

Elas recebem um objeto request, fazem algum processamento e retornam uma resposta HTTP (HttpResponse ou render).

Exemplo de uma função simples:

    def home(request):
        return HttpResponse("Olá mundo!")


Como elas funcionam?

• Qualquer view recebe pelo menos o parâmetro request

• A lógica fica toda dentro da função

• Podem usar condicionais como if request.method == "POST"

• Ideais para quem está começando por serem intuitivas




### 1. Estrutura do CRUD

Vamos criar um novo projeto para exemplificar um crud.


| Ação    | View             | Método   | Template    |
| ------- | ---------------- | -------- | ----------- |
| Listar  | `produto_list`   | GET      | list.html   |
| Criar   | `produto_create` | GET/POST | form.html   |
| Editar  | `produto_update` | GET/POST | form.html   |
| Deletar | `produto_delete` | GET/POST | delete.html |


1.1 Criar o projeto e o app

Abra o terminal e digite :

    django-admin startproject loja
    cd loja
    python manage.py startapp produtos

Ativando o app no settings.py:

    INSTALLED_APPS = [
        ...
        'produtos',
    ]

1.2 Criar o Model
    
    from django.db import models

    class Produto(models.Model):
        nome = models.CharField(max_length=100)
        preco = models.DecimalField(max_digits=6, decimal_places=2)
        descricao = models.TextField()
    
        def __str__(self):
            return self.nome

Abra o temrinal e digite : 
    
    python manage.py makemigrations
    python manage.py migrate

1.3 Criar o Formulário

Criamos um arquivo: produtos/forms.py

    from django import forms
    from .models import Produto
    
    class ProdutoForm(forms.ModelForm):
        class Meta:
            model = Produto
            fields = ['nome', 'preco', 'descricao']

1.4 Criar as Views (FBV)
   
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
    

1.5 Criar URLs

    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('', views.produto_list, name='produto_list'),
        path('novo/', views.produto_create, name='produto_create'),
        path('editar/<int:pk>/', views.produto_update, name='produto_update'),
        path('deletar/<int:pk>/', views.produto_delete, name='produto_delete'),
    ]

No arquivo loja/urls.py:
    
    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('produtos/', include('produtos.urls')),
    ]

1.6 Templates

Para os tamplates verificar os arquivos na pasta 

    loja/produtos/templates



### Cronograma das Aulas 

| Aula	                                                 | Branch  |                                                 Clique no Link |
|:------------------------------------------------------|:-------:|---------------------------------------------------------------:|
| Aula 1 – O que é Django?                              | aula_1  |              [Link](https://github.com/SANDEISON/curso_django) |
| Aula 2 - Configuração do Ambiente Django              | aula_2  |  [Link](https://github.com/SANDEISON/curso_django/tree/aula_2) |
| Aula 3 - Criação e Estrutura do Projeto em Django     | aula_3  |  [Link](https://github.com/SANDEISON/curso_django/tree/aula_3) |
| Aula 4 - Templates no Django                          | aula_4  |  [Link](https://github.com/SANDEISON/curso_django/tree/aula_4) |
| Aula 5 - Models e Banco de Dados no Django (ORM)      | aula_5  |  [Link](https://github.com/SANDEISON/curso_django/tree/aula_5) |
| Aula 6 - Exibindo dados do Models no Template         | aula_6  |  [Link](https://github.com/SANDEISON/curso_django/tree/aula_6) |
| Aula 7 - Enviando dados do Template para a view       | aula_7  |  [Link](https://github.com/SANDEISON/curso_django/tree/aula_7) |
| Aula 8 - Relacionamentos no Django                    | aula_8  |  [Link](https://github.com/SANDEISON/curso_django/tree/aula_8) |
| Aula 9 - Explorando o Painel Administrativo do Django | aula_9  |  [Link](https://github.com/SANDEISON/curso_django/tree/aula_9) |
| Aula 10 - Views Baseadas em Função (FBV)              | aula_10 | [Link](https://github.com/SANDEISON/curso_django/tree/aula_10) |
| Aula 11 - Views Baseadas em Classe (CBV)              | aula_11 | [Link](https://github.com/SANDEISON/curso_django/tree/aula_11) |