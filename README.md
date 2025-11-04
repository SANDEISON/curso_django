# 📘Curso de Django (Python)

## 🔹 Aula 11 – Views Baseadas em Classe (CBV)

As Class Based Views são views implementadas como classes Python, o que traz muita organização e reaproveitamento de código. 

O Django já oferece views genéricas prontas para operações comuns, como listar, criar, atualizar e deletar objetos.

Você não precisa reinventar a roda. O Django já deixa a roda balanceada e ainda te entrega o carro junto

##### Vantagens das CBVs

| Benefício       | Por quê?                                   |
| --------------- | ------------------------------------------ |
| Reutilização    | Herdamos comportamentos prontos            |
| Organização     | Código mais limpo e modular                |
| Extensibilidade | Fácil adicionar comportamentos específicos |
| Menos repetição | DRY total (Don't Repeat Yourself)          |



### 1. Estrutura do CRUD

Vamos utilizar o mesmo projeto para exemplificar um crud com o CBV.

| Ação    | View             | Método   | Template    |
| ------- | ---------------- | -------- | ----------- |
| Listar  | `produto_list`   | GET      | list.html   |
| Criar   | `produto_create` | GET/POST | form.html   |
| Editar  | `produto_update` | GET/POST | form.html   |
| Deletar | `produto_delete` | GET/POST | delete.html |


1.1 Criar o projeto e o app

Abra o terminal e digite :

    django-admin startproject loja .
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

1.4 Views usando CBV
   
    from django.urls import reverse_lazy
    from django.views.generic import ListView, CreateView, UpdateView, DeleteView
    from .models import Produto
    from .forms import ProdutoForm
    
    
    class ProdutoListView(ListView):
        model = Produto
        template_name = 'produtos/list.html'
        context_object_name = 'produtos'
    
    
    class ProdutoCreateView(CreateView):
        model = Produto
        form_class = ProdutoForm
        template_name = 'produtos/form.html'
        success_url = reverse_lazy('produto_list')
    
    
    class ProdutoUpdateView(UpdateView):
        model = Produto
        form_class = ProdutoForm
        template_name = 'produtos/form.html'
        success_url = reverse_lazy('produto_list')
    
    
    class ProdutoDeleteView(DeleteView):
        model = Produto
        template_name = 'produtos/delete.html'
        success_url = reverse_lazy('produto_list')


1.5 Criar URLs

    from django.urls import path
    from .views import (
        ProdutoListView, ProdutoCreateView,
        ProdutoUpdateView, ProdutoDeleteView
    )
    
    urlpatterns = [
        path('', ProdutoListView.as_view(), name='produto_list'),
        path('novo/', ProdutoCreateView.as_view(), name='produto_create'),
        path('editar/<int:pk>/', ProdutoUpdateView.as_view(), name='produto_update'),
        path('deletar/<int:pk>/', ProdutoDeleteView.as_view(), name='produto_delete'),
    ]

No arquivo loja/urls.py:
    
    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('produtos/', include('produtos.urls')),
    ]

1.6 Templates

Os mesmos templates usados no FBV funcionam aqui também.

Para os tamplates verificar os arquivos na pasta 
   
    loja/produtos/templates


| Template    | Usado por               |
| ----------- | ----------------------- |
| base.html   | Todos                   |
| list.html   | ListView                |
| form.html   | CreateView e UpdateView |
| delete.html | DeleteView              |

1.7 Resumo do CRUD com CBV

| Ação    | View Genérica | O que ela entrega                        |
| ------- | ------------- | ---------------------------------------- |
| Listar  | ListView      | Busca os objetos e passa para o template |
| Criar   | CreateView    | Formulário pronto e validação            |
| Editar  | UpdateView    | Form preenchido com os dados             |
| Deletar | DeleteView    | Busca e exclui o objeto com confirmação  |



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