# 📘 Curso de Django com Python

## 🔹 Aula 3 – Criação e estrutura do projeto

Nesta aula, vamos instalar o Django, criar o primeiro projeto, conhecer os arquivos gerados e desenvolver uma rota simples para o app `blog`.

## 🎯 Objetivos da aula

Ao final desta aula, você será capaz de:

- instalar e verificar o Django;
- criar um projeto Django;
- compreender a função dos principais arquivos do projeto;
- executar migrações e iniciar o servidor de desenvolvimento;
- criar e registrar um app;
- implementar uma view simples;
- conectar as URLs do app às URLs do projeto;
- registrar as dependências no `requirements.txt`.

## 📍 Pré-requisitos

Antes de começar, confirme se:

- o Python está instalado;
- o ambiente virtual `.venv` foi criado;
- o ambiente virtual está ativo;
- o terminal está aberto na pasta do projeto.

Com o ambiente ativo, o terminal normalmente exibe `(.venv)` antes do caminho atual.

## 1. Instalação do Django

Se você clonou esta branch do repositório, instale as dependências registradas:

```powershell
python -m pip install -r requirements.txt
```

Se estiver reproduzindo a aula manualmente, instale a mesma versão utilizada pelo projeto:

```powershell
python -m pip install "Django==5.2.5"
```

Verifique a versão instalada:

```powershell
python -m django --version
```

> Utilizar `python -m pip` e `python -m django` ajuda a garantir que os comandos sejam executados pelo Python do ambiente virtual ativo.

## 2. Criação do primeiro projeto

Na pasta em que o projeto será desenvolvido, execute:

```powershell
django-admin startproject meu_projeto .
```

O ponto final (`.`) indica que os arquivos devem ser criados no diretório atual. Sem ele, o Django criaria outra pasta externa chamada `meu_projeto`.

Depois dos comandos desta aula, a estrutura será semelhante a:

```text
curso_django/
├── manage.py
├── requirements.txt
├── meu_projeto/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── blog/
    ├── migrations/
    │   └── __init__.py
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

### 2.1 Principais arquivos do projeto

#### `manage.py`

Utilitário de linha de comando utilizado para administrar o projeto. Com ele, podemos iniciar o servidor, criar apps, executar migrações e realizar outras tarefas.

```powershell
python manage.py nome_do_comando
```

#### `meu_projeto/__init__.py`

Indica ao Python que o diretório pode ser tratado como um pacote. Normalmente, esse arquivo permanece vazio.

#### `meu_projeto/settings.py`

Contém as configurações gerais, incluindo:

- apps instalados (`INSTALLED_APPS`);
- banco de dados;
- idioma e fuso horário;
- templates;
- middlewares;
- arquivos estáticos.

#### `meu_projeto/urls.py`

Define as rotas principais do projeto. Inicialmente, o Django configura a rota do painel administrativo:

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
```

#### `meu_projeto/wsgi.py` e `meu_projeto/asgi.py`

- **WSGI:** interface utilizada por servidores web tradicionais para executar aplicações Python.
- **ASGI:** interface que também oferece suporte a recursos assíncronos, como conexões persistentes.

Normalmente, esses arquivos não precisam ser alterados durante o desenvolvimento inicial.

## 3. Preparação do banco de dados

O Django inclui apps internos para autenticação, sessões e painel administrativo. Execute as migrações iniciais para criar as tabelas utilizadas por esses recursos:

```powershell
python manage.py migrate
```

Nesta etapa, o projeto utiliza o SQLite por padrão. O arquivo local `db.sqlite3` será criado na raiz do projeto e não deve ser versionado neste curso.

## 4. Execução do servidor de desenvolvimento

Inicie o servidor:

```powershell
python manage.py runserver
```

O terminal apresentará um endereço semelhante a:

```text
Starting development server at http://127.0.0.1:8000/
```

Acesse [http://127.0.0.1:8000/](http://127.0.0.1:8000/) no navegador. A página inicial do Django confirma que o projeto está funcionando.

Para encerrar o servidor, pressione `Ctrl + C` no terminal.

> O comando `runserver` deve ser utilizado somente durante o desenvolvimento. Em produção, a aplicação precisa ser executada por um servidor apropriado.

## 5. Criação do app `blog`

Um **projeto** reúne as configurações gerais do site. Um **app** representa uma funcionalidade específica, como blog, produtos, pedidos ou usuários. Um mesmo projeto pode conter diversos apps.

Crie o app `blog`:

```powershell
python manage.py startapp blog
```

O comando cria os seguintes arquivos principais:

- `admin.py`: integra os models ao painel administrativo;
- `apps.py`: define a configuração do app;
- `migrations/`: armazena o histórico de alterações do banco de dados;
- `models.py`: define os dados e relacionamentos da aplicação;
- `tests.py`: recebe os testes automatizados;
- `views.py`: recebe funções ou classes que processam requisições.

> O arquivo `blog/urls.py` não é criado automaticamente. Ele será adicionado manualmente na seção 7.

## 6. Registro do app no projeto

Abra `meu_projeto/settings.py` e adicione a configuração do app em `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog.apps.BlogConfig",
]
```

O registro permite que o Django reconheça os models, as migrações e outras configurações do app.

## 7. Criação da primeira view

Abra `blog/views.py` e crie a função `home`:

```python
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Bem-vindo ao Blog!</h1>")
```

A view recebe o objeto `request` e devolve uma resposta HTTP com o texto que será exibido no navegador.

## 8. Configuração das URLs

### 8.1 URLs do app

Crie manualmente o arquivo `blog/urls.py`:

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
]
```

A rota vazia representa a página inicial dentro do prefixo que será definido pelo projeto.

### 8.2 URLs do projeto

Abra `meu_projeto/urls.py`, importe `include` e conecte as URLs do app:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
]
```

O Django combina o prefixo `blog/`, definido no projeto, com a rota vazia do app. Por isso, a view `home` fica disponível no endereço `/blog/`.

## 9. Teste da aplicação

Execute novamente o servidor:

```powershell
python manage.py runserver
```

Acesse [http://127.0.0.1:8000/blog/](http://127.0.0.1:8000/blog/) no navegador. A página deverá exibir:

```text
Bem-vindo ao Blog!
```

## 10. Registro das dependências

Como o Django foi instalado nesta aula, registre as dependências do ambiente:

```powershell
python -m pip freeze > requirements.txt
```

Ao baixar o projeto em outro computador, as dependências podem ser instaladas com:

```powershell
python -m pip install -r requirements.txt
```

## ✅ Checklist da aula

Antes de avançar, confirme se:

- [ ] o ambiente virtual está ativo;
- [ ] `python -m django --version` exibe a versão instalada;
- [ ] `python manage.py migrate` foi executado;
- [ ] o app `blog` está registrado em `INSTALLED_APPS`;
- [ ] `python manage.py runserver` inicia sem erros;
- [ ] `/blog/` exibe a mensagem de boas-vindas;
- [ ] o arquivo `requirements.txt` contém o Django e suas dependências.

## 🗓️ Cronograma das aulas

| Aula                                                   | Branch  | Acesso                                                        |
|:-------------------------------------------------------|:-------:|:--------------------------------------------------------------|
| Aula 1 – O que é Django?                               | aula_1  | [Link](https://github.com/SANDEISON/curso_django/tree/aula_1)  |
| Aula 2 – Configuração do ambiente Django              | aula_2  | [Link](https://github.com/SANDEISON/curso_django/tree/aula_2)  |
| Aula 3 – Criação e estrutura do projeto em Django     | aula_3  | [Link](https://github.com/SANDEISON/curso_django/tree/aula_3)  |
| Aula 4 – Templates no Django                          | aula_4  | [Link](https://github.com/SANDEISON/curso_django/tree/aula_4)  |
| Aula 5 – Models e banco de dados no Django (ORM)      | aula_5  | [Link](https://github.com/SANDEISON/curso_django/tree/aula_5)  |
| Aula 6 – Exibindo dados dos models no template        | aula_6  | [Link](https://github.com/SANDEISON/curso_django/tree/aula_6)  |
| Aula 7 – Enviando dados do template para a view       | aula_7  | [Link](https://github.com/SANDEISON/curso_django/tree/aula_7)  |
| Aula 8 – Relacionamentos no Django                    | aula_8  | [Link](https://github.com/SANDEISON/curso_django/tree/aula_8)  |
| Aula 9 – Explorando o painel administrativo do Django | aula_9  | [Link](https://github.com/SANDEISON/curso_django/tree/aula_9)  |
| Aula 10 – Views baseadas em função (FBV)              | aula_10 | [Link](https://github.com/SANDEISON/curso_django/tree/aula_10) |
| Aula 11 – Views baseadas em classe (CBV)              | aula_11 | [Link](https://github.com/SANDEISON/curso_django/tree/aula_11) |
| Aula 12 – Django REST Framework                       | aula_12 | [Link](https://github.com/SANDEISON/curso_django/tree/aula_12) |
| Aula 13 – Autenticação por Token e JWT                | aula_13 | [Link](https://github.com/SANDEISON/curso_django/tree/aula_13) |
