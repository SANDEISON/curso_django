# 📘Curso de Django (Python)

## 🔹 Aula 7 – Enviando dados do Template para a view

No Django, o fluxo normal é: da view para o template (passando dados pelo contexto).
Mas também é possível enviar informações do template para a view, geralmente de duas formas:

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

1.2 Template Home

    {% extends "base.html" %}
    {% block content %}
      <ul>
        {% for i in posts %}
          <li>{{ i.titulo }}</li>
        {% endfor %}
      </ul>
    
    {% endblock %}

1.3 Arquivo views

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


Obs: Foi adicionado a classe Pessoa no models , para podemos visualizar mais de uma classe no django admin. É necessário atualizar o projeto com os comandos abaixo:

No terminal digite:

    python manage.py makemigrations

No terminal digite :

    python manage.py migrate


### Cronograma das Aulas 

| Aula	                                             | Branch |                                                Clique no Link |
|:--------------------------------------------------|:------:|--------------------------------------------------------------:|
| Aula 1 – O que é Django?                          | aula_1 |             [Link](https://github.com/SANDEISON/curso_django) |
| Aula 2 - Configuração do Ambiente Django          | aula_2 | [Link](https://github.com/SANDEISON/curso_django/tree/aula_2) |
| Aula 3 - Criação e Estrutura do Projeto em Django | aula_3 | [Link](https://github.com/SANDEISON/curso_django/tree/aula_3) |
| Aula 4 - Templates no Django                      | aula_4 | [Link](https://github.com/SANDEISON/curso_django/tree/aula_4) |
| Aula 5 - Models e Banco de Dados no Django (ORM)  | aula_5 | [Link](https://github.com/SANDEISON/curso_django/tree/aula_5) |
| Aula 6 - Exibindo dados do Models no Template     | aula_6 | [Link](https://github.com/SANDEISON/curso_django/tree/aula_6) |
| Aula 7 - Enviando dados do Template para a view     | aula_7 | [Link](https://github.com/SANDEISON/curso_django/tree/aula_7) |
| Aula 8 - Relacionamentos no Django     | aula_8 | [Link](https://github.com/SANDEISON/curso_django/tree/aula_8) |
