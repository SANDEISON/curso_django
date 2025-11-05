# 📘Curso de Django Rest Framework, ou DRF

![img.png](img.png)


### 1. Autenticação por Token e JWT no Django REST Framework

O Django REST Framework (DRF) oferece diferentes formas de autenticação:

| Tipo      | Armazenamento                          | Expiração                   | Segurança | Recomendado para                 |
| --------- | -------------------------------------- | --------------------------- | --------- | -------------------------------- |
| **Token** | Banco de dados                         | Não expira (padrão)         | Média     | APIs simples, testes internos    |
| **JWT**   | Não armazenado no servidor (stateless) | Sim, expira automaticamente | Alta      | APIs modernas, apps SPA e mobile |




### 2. Autenticação por TOKEN (clássica do DRF)

2.1. Instalação e Configuração

    pip install django djangorestframework
    pip install djangorestframework-authtoken


No settings.py, adicione:

    INSTALLED_APPS = [
        'rest_framework',
        'rest_framework.authtoken',  # 🔹 necessário para TokenAuth
        'accounts',
    ]


E configure o DRF:

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
        ),
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        ),
    }


2.2. Criando o modelo e serializer

Arquivo: accounts/models.py

    from django.db import models
    from django.contrib.auth.models import User
    
    class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        bio = models.TextField(blank=True)
    
        def __str__(self):
            return self.user.username
    

Arquivo: accounts/serializers.py

    from rest_framework import serializers
    from django.contrib.auth.models import User
    from .models import Profile
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['id', 'username', 'email']
    
    class ProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile
            fields = '__all__'



2.3. ViewSets

Arquivo: accounts/views.py

    from rest_framework import viewsets, permissions
    from .models import Profile
    from .serializers import ProfileSerializer
    
    class ProfileViewSet(viewsets.ModelViewSet):
        queryset = Profile.objects.all()
        serializer_class = ProfileSerializer
        permission_classes = [permissions.IsAuthenticated]




2.4. URLs e Endpoint de Token

Arquivo: accounts/urls.py

    from django.urls import path, include
    from rest_framework.routers import DefaultRouter
    from .views import ProfileViewSet
    from rest_framework.authtoken.views import obtain_auth_token
    
    router = DefaultRouter()
    router.register(r'profiles', ProfileViewSet)
    
    urlpatterns = [
        path('', include(router.urls)),
        path('token/', obtain_auth_token, name='api_token_auth'),
    ]

Arquivo: user_api/urls.py

    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/', include('accounts.urls')),
    ]



2.5. Como usar


Obtenha o token de autenticação:

POST /api/token/
{
  "username": "admin",
  "password": "admin"
}


Resposta:

    {
      "token": "cd46f14c6a1df5b61b22cf3e4f0..."
    }

Use o token em cada requisição:

    Authorization: Token cd46f14c6a1df5b61b22cf3e4f0...

🧩 Vantagens:

- Fácil de configurar.

- Ideal para projetos pequenos ou APIs internas.

⚠️ Desvantagens:

- Token fixo (não expira).

- Armazenado no banco de dados (menos escalável).

- Precisa de limpeza manual em revogações.


### 3. Autenticação por JWT (JSON Web Token)

3.1. Instalação e Configuração

    pip install djangorestframework-simplejwt

No settings.py:

    INSTALLED_APPS += ['rest_framework']
    
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),
    }


3.2. Endpoints JWT

Arquivo: accounts/urls.py

    from django.urls import path, include
    from rest_framework.routers import DefaultRouter
    from .views import ProfileViewSet
    from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )
    
    router = DefaultRouter()
    router.register(r'profiles', ProfileViewSet)
    
    urlpatterns = [
        path('', include(router.urls)),
        path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]


3.3. Obter Tokens JWT

Login:

    POST /api/token/
    {
      "username": "admin",
      "password": "admin"
    }

Resposta:

    {
      "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
      "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
    }

Usar o token:

    Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...

Renovar:

    POST /api/token/refresh/
    {
      "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
    }


### 4. Diferenças Internas (como funciona o JWT)

- O servidor gera o token com base em uma chave secreta (SECRET_KEY).

- Ele não salva nada no banco — tudo está dentro do token (usuário, tempo de expiração etc.).

- O cliente envia o token a cada requisição.

- O servidor valida o token decodificando e verificando a assinatura.

- Quando o token expira, o cliente usa o refresh token para pedir um novo.


### 5. Comparativo Técnico


| Característica                            | Token Auth (DRF)            | JWT Auth                       |
| ----------------------------------------- | --------------------------- | ------------------------------ |
| Armazenamento                             | Banco de dados              | Nenhum (stateless)             |
| Expiração                                 | Não expira                  | Expira automaticamente         |
| Validação                                 | Busca o token no banco      | Validação criptográfica        |
| Performance                               | Mais lenta (consulta no DB) | Mais rápida                    |
| Revogação manual                          | Fácil (deleta token do DB)  | Difícil (depende de blacklist) |
| Uso em APIs modernas (React, Vue, Mobile) | Limitado                    | Ideal                          |


### 6. Qual usar?


| Cenário                                             | Recomendação      |
| --------------------------------------------------- | ----------------- |
| API simples, interna, sem frontend separado         | Token tradicional |
| API pública, SPA, mobile app, microserviços         | JWT (SimpleJWT)   |
| Precisa revogar tokens facilmente                   | Token tradicional |
| Precisa escalar horizontalmente (vários servidores) | JWT               |





### Conclusão

- TokenAuth: simples, rápido de configurar, mas com limitações.
- JWTAuth: mais robusto, seguro e escalável — padrão atual em APIs REST.


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