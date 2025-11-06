# 📘Curso de Django Rest Framework, ou DRF

![img.png](img.png)


A diferença entre Django e Django REST Framework (DRF) está principalmente no propósito e na forma como cada um trata a comunicação entre o servidor e o cliente.


### 1. Django

- É um framework web completo em Python para criar aplicações baseadas em páginas HTML.

- Ele é ideal quando você quer criar sites tradicionais, com páginas renderizadas no servidor (ex.: HTML, templates, formulários, etc).

Exemplo:

    # views.py
    from django.shortcuts import render
    from .models import Usuario
    
    def listar_usuarios(request):
        usuarios = Usuario.objects.all()
        return render(request, 'usuarios.html', {'usuarios': usuarios})





### 2. Django REST Framework (DRF)

- É uma extensão do Django voltada para criar APIs RESTful.

- Em vez de enviar HTML, ele envia dados em formato JSON (ou XML), para serem consumidos por aplicações frontend (como React, Vue, Angular) ou apps mobile.

- Ele adiciona ferramentas para serialização, autenticação, autorização, paginação, e versionamento de APIs.
    
Exemplo:

Você cria uma view que retorna JSON, não HTML:


    # views.py
    from rest_framework import viewsets
    from .models import Usuario
    from .serializers import UsuarioSerializer
    
    class UsuarioViewSet(viewsets.ModelViewSet):
        queryset = Usuario.objects.all()
        serializer_class = UsuarioSerializer


E o serializer transforma o modelo em JSON:

    # serializers.py
    from rest_framework import serializers
    from .models import Usuario
    
    class UsuarioSerializer(serializers.ModelSerializer):
        class Meta:
            model = Usuario
            fields = '__all__'


O resultado será algo assim:

    [
      {"id": 1, "nome": "João", "email": "joao@email.com"},
      {"id": 2, "nome": "Maria", "email": "maria@email.com"}
    ]




### 2. Django REST Framework (DRF)


| Característica    | **Django**                        | **Django REST Framework (DRF)**        |
| ----------------- | --------------------------------- | -------------------------------------- |
| Objetivo          | Criar sites e sistemas web (HTML) | Criar APIs REST (JSON)                 |
| Retorno principal | Páginas HTML renderizadas         | Dados em JSON                          |
| Comunicação       | Cliente consome páginas           | Cliente consome dados (front separado) |
| Uso comum         | Sites, portais, sistemas internos | APIs para apps, SPAs, integrações      |
| Templates         | Usa Django Templates              | Não usa templates, usa Serializers     |
| Autenticação      | Session, User padrão do Django    | Token, JWT, OAuth, etc.                |




### 3. O que é uma API REST?

- API (Application Programming Interface) é uma forma de um sistema se comunicar com outro.
- REST (Representational State Transfer) é um padrão que define como criar APIs usando HTTP.

Princípios REST:

- Stateless: cada requisição é independente.

- Recursos (Resources): são entidades (ex: usuários, produtos).

Métodos HTTP:

- GET: ler dados

- POST: criar dados

- PUT/PATCH: atualizar dados

- DELETE: remover dados



### 3. Como criar um Projeto Django REST Framework

Passos iniciais:


    # Criar e ativar ambiente virtual
    python -m venv venv
    venv\Scripts\activate  # (Windows: venv\Scripts\activate)
    
    # Instalar Django e DRF
    pip install django djangorestframework
    
    # Criar projeto
    django-admin startproject apiprojeto .
    
    # Criar app
    python manage.py startapp api




### 4. Configuração inicial

No arquivo settings.py:

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',  # DRF
        'api',             # Nosso app
    ]


### 5.Criando o Modelo (models.py)

Exemplo de modelo de Postagem:

    from django.db import models
    
    class Post(models.Model):
        titulo = models.CharField(max_length=100)
        conteudo = models.TextField()
        data_criacao = models.DateTimeField(auto_now_add=True)
    
        def __str__(self):
            return self.titulo

No terminal digite:

    python manage.py makemigrations
    python manage.py migrate



### 6. Serializers

Os Serializers convertem objetos do Django (modelos) em formatos JSON, e vice-versa.

Arquivo: api/serializers.py
    
    from rest_framework import serializers
    from .models import Post
    
    class PostSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = '__all__'




### 7. ViewSets

Os ViewSets gerenciam automaticamente as operações CRUD.

Suas responsabilidades são:

- Receber os dados da Requisição (formato JSON ou XML)
- Validar os dados de acordo com as regras definidas na modelagem e no Serializer
- Desserializar a Requisição e instanciar objetos
- Processar regras de negócio (aqui é onde implementamos a lógica dos nossos sistemas)
- Formular uma resposta e responder a quem chamou sua API



Arquivo: api/views.py

    from rest_framework import viewsets
    from .models import Post
    from .serializers import PostSerializer
    
    class PostViewSet(viewsets.ModelViewSet):
        queryset = Post.objects.all()
        serializer_class = PostSerializer


### 8. Endpoints REST com Router

Arquivo: api/urls.py

    from django.urls import path, include
    from rest_framework.routers import DefaultRouter
    from .views import PostViewSet
    
    router = DefaultRouter()
    router.register(r'posts', PostViewSet, basename='post')
    
    urlpatterns = [
        path('', include(router.urls)),
    ]



Arquivo: apiprojeto/urls.py

    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/', include('api.urls')),
    ]
    
digite no terminal:  

    python manage.py runserver


Agora, acesse no navegador:

http://127.0.0.1:8000/api/posts/

Você verá a interface interativa do Django REST Framework.




### 9. Resumo 
O processo de desenvolvimento de aplicações que utilizam o Django Rest Framework geralmente seguem a seguinte linha de implementação:

1) Modelagem
2) Serializers
3) ViewSets
4) Routers





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
| Aula 12 - Django Rest Framework                       | aula_12 | [Link](https://github.com/SANDEISON/curso_django/tree/aula_12) |
| Aula 13 - Autenticação por Token e JWT                       | aula_13 | [Link](https://github.com/SANDEISON/curso_django/tree/aula_13) |