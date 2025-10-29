# 📘Curso de Django (Python)

## 🔹 Aula 7 – Enviando dados do Template para a view

No Django, o fluxo normal é: da view para o template (passando dados pelo contexto).
Mas também é possível enviar informações do template para a view.

Quando a gente quer pegar o que o usuário digitou em uma página HTML e 
mandar para o backend no Django, existe um pequeno “caminho” que precisa ser construído. 
O HTML coleta os dados, o navegador envia esses dados, Django recebe, valida, 
processa e então faz algo com isso (salvar no banco, por exemplo).

### 1. Usando Formulários HTML

Se você tem um <form> no template, pode enviar os dados para a view com POST.

Para este exemplo vamos utilizar três arquivos, tela de login, tela de home e a view login

1.1 Template login
    
    {% extends "base.html" %}
    {% block content %}
      <form method="post" action="{% url 'login' %}">
        {% csrf_token %}
        <input type="text" name="nome" placeholder="Digite seu nome">
        <input type="password" name="senha" placeholder="Digite sua senha">
        <button type="submit">Enviar</button>
      </form>
    {% endblock %}


Nos campos que tenham o atributo name definido. É o name que o Django vai usar para recuperar a informação.

Repare no:

method="POST" para enviar com segurança

{% csrf_token %} para o Django aceitar essa requisição

1.2 Template Home

    {% extends "base.html" %}
    {% block content %}
      <ul>
        {% for i in posts %}
          <li>{{ i.titulo }}</li>
        {% endfor %}
      </ul>
    
    {% endblock %}


1.3 Uma rota (URL) que receba o POST

No arquivo blog/urls.py podemos ver a rota criada

    urlpatterns = [
        path('', views.login, name='login'),
    ]

1.4 Arquivo view

    from django.shortcuts import render
    from blog.models import Post
    # Create your views here.
    
    def login(request):
        if request.method == "POST":
            nome = request.POST.get("nome")
            senha = request.POST.get("senha")
            posts = Post.objects.all().values()
            print(nome)
            print(senha)
            return render(request, 'home.html', locals())
    
        return render(request, 'login.html', locals())



### 2. Usando Formulários com o ModelForm
O ModelForm é um tipo de formulário do Django que é criado automaticamente com base em um Model.

Isso reduz repetição de código, já que o formulário já possui os campos do Model e validações embutidas.

2.1 Criando o ModelForm

Dentro da pasta blog criamos um arquivo forms.py

    from django import forms
    from .models import Post
    
    class PostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ['titulo', 'conteudo']

2.2 Views: listar e editar Post
 
Dentro do arquivo blog/views.py criamos os metodos de listar e editar

    from django.shortcuts import render, get_object_or_404, redirect
    from .models import Post
    from .forms import PostForm
    
    def post_list(request):
        posts = Post.objects.all().order_by('-data_criacao')
        return render(request, 'blog/post_list.html', {'posts': posts})
    
    def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST or None, instance=post)
    
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('post_list')
    
        return render(request, 'blog/post_edit.html', {'form': form})

2.3 Templates

Criamos dois templates um para listar e outro para editar

Template de Listagem: post_list.html

    <h1>Posts Cadastrados</h1>

    <table border="1" cellpadding="8">
        <tr>
            <th>Título</th>
            <th>Data</th>
            <th>Ações</th>
        </tr>
    
        {% for post in posts %}
        <tr>
            <td>{{ post.titulo }}</td>
            <td>{{ post.data_criacao|date:"d/m/Y H:i" }}</td>
            <td>
                <a href="{% url 'post_edit' post.pk %}">Editar</a>
            </td>
        </tr>
        {% endfor %}
    </table>



Template de Edição: post_edit.html

    <h2>Editar Post</h2>
    
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Salvar</button>
    </form>
    
    <a href="{% url 'post_list' %}">Voltar</a>


2.4 Configurando URLs

No arquivo blog/urls.py adicionamos as novas rotas

    from .views import post_edit, post_list
    
    urlpatterns = [
        path('', views.login, name='login'),
        path('posts/', post_list, name='post_list'),
        path('posts/<int:pk>/editar/', post_edit, name='post_edit'),
    ]

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