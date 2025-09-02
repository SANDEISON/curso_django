# 📘Curso de Django (Python)

## 🔹 Aula 4 – Templates no Django

### 1. Criando a Pasta de Templates

Dentro do app blog/, crie a pasta templates/ e dentro dela um arquivo home.html:

    blog/
    ├── templates/
    │   └── home.html
    ├── views.py
    ├── urls.py
    ...

Exemplo home.html

    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Blog - Página Inicial</title>
    </head>
    <body>
        <h1>Bem-vindo ao Blog!</h1>
        <p>Este é o meu primeiro template no Django 🎉</p>
    </body>
    </html>



### 2. Alterando a View para Usar Templates

No arquivo blog/views.py:

    from django.shortcuts import render
    
    def home(request):
        return render(request, 'home.html')



### 3. Instalando o Bootstrap 5 no django

3.1 Ative o ambiente virtual:

    venv\Scripts\activate

3.2 Uma vez dentro do ambiente virtual, instale o Bootstrap 5 com este comando:

    pip install django-bootstrap-v5

3.3 Atualizar configurações

O próximo passo é incluir o módulo bootstrap na INSTALLED_APPSlista em settings.py:

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'blog',  # app criado
        'bootstrap5', #Bootstrap 5
    ]

3.4 Adicionar Bootstrap 5 ao modelo

Dentro da pasta template crie um arquivo HTML base.html
e adicione o Bootstrap
    
    <!DOCTYPE html>
    <html>
    <head>
      <title>{% block title %}{% endblock %}</title>
      {% load bootstrap5 %}
      {% bootstrap_css %}
      {% bootstrap_javascript %}
    </head>
    <body>
    
    <div class="container">
      <ul class="nav bg-info">
        <li class="nav-item">
          <a class="nav-link link-light" href="/">HOME</a>
        </li>
        <li class="nav-item">
          <a class="nav-link link-light" href="/members">MEMBERS</a>
        </li>
      </ul>
    
      {% block content %}
      {% endblock %}
    </div>
    </body>
    </html>

Como você pode ver, inserimos essas três linhas na seção <head> :

    {% load bootstrap5 %}
    {% bootstrap_css %}
    {% bootstrap_javascript %}

A primeira linha informa ao Django que ele deve carregar o módulo Bootstrap 5 neste modelo.

A segunda linha insere o

    <link> 

elemento com a referência à folha de estilo do bootstrap.

A terceira linha insere o 

    <script> 

elemento com a referência ao arquivo javascript necessário.

Pronto! O Bootstrap 5 agora faz parte do seu projeto!

Podemos acessar os modelos do Bootstrap em 

Link : https://getbootstrap.com/


3.5 Alterando o home.html

Vamos fazer uma alteração no arquivo home.html
incluindo os dados do arquivo base.html

    {% extends "base.html" %}
    
    
    {% block content %}
    
        <h2>Bem-vindo , inciando com Django</h2>
    
    {% endblock %}


### 4. Exemplo utilizando o Bootstrap

No arquivo home.html adicione o seguinte código.


    {% extends "base.html" %}
    {% block content %}
        <div class="container-fluid">
            <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">Email address</label>
                <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
            </div>
            <div class="mb-3">
                <label for="exampleFormControlTextarea1" class="form-label">Example textarea</label>
                <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
            </div>
        </div>
    {% endblock %}


Para finalizar esta aula, como adicionamos do Django no projeto, vamos incluir as dependências no arquivo requirements.txt

No terminal digite :

    pip freeze > requirements.txt