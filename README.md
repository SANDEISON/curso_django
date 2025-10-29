# 📘Curso de Django (Python)

## 🔹 Aula 5 – Models e Banco de Dados no Django (ORM)

### 1. ORM (Object-Relational Mapping)

O ORM (Object-Relational Mapping) do Django permite manipular bancos de dados usando código Python, sem precisar escrever SQL diretamente.

1.1 Configuração do Banco de Dados

Por padrão, o Django usa SQLite (leve e já embutido no projeto).
No arquivo settings.py você verá algo assim:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
É possível trocar para PostgreSQL, MySQL ou outros bancos apenas alterando essas configurações.


### 2. Criando as Migrações

2.1 Criar a migração

No terminal digite :

    python manage.py makemigrations

Saída esperada:

Migrations for 'blog':
  blog/migrations/0001_initial.py

2.2 Aplicar no banco de dados:

No terminal digite :

    python manage.py migrate


### 3.Criando um Model (Tabela)

Dentro do app blog, edite o arquivo models.py:
    
    from django.db import models
    
    class Post(models.Model):
        titulo = models.CharField(max_length=200)
        conteudo = models.TextField()
        data_criacao = models.DateTimeField(auto_now_add=True)
    
        def __str__(self):
            return self.titulo

Explicação dos campos:

CharField → Texto curto, com limite de caracteres.

TextField → Texto longo (sem limite específico).

DateTimeField → Data e hora; auto_now_add=True insere automaticamente a data de criação.

__str__ → Define como o objeto será exibido no painel admin ou no shell.


Depois de criar/alterar models, precisamos gerar as migrações (instruções para criar tabelas no banco).

No terminal digite :

    python manage.py makemigrations

No terminal digite :

    python manage.py migrate


### 4. Django Admin

Django Admin é uma ferramenta realmente ótima no Django, na verdade é uma interface de usuário CRUD* de todos os seus modelos!

É gratuito e vem pronto para uso com Django:

1.1 Iniciando com o Django Admin

Para entrar na interface do usuário do administrador, inicie o servidor navegando

No terminal digite :

    python manage.py runserver

Na janela do navegador, digite 127.0.0.1:8000/admin/na barra de endereço.

Ao acessar você vera uma tela de login.


O motivo pelo qual esta URL leva à página de login do administrador do Django pode ser encontrado no urls.py arquivo do seu projeto:


    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('blog/', include('blog.urls')),  # rota do app blog
    ]



1.2  Criar Usuário no Django Admin 

Para poder efetuar login no aplicativo de administração, precisamos criar um usuário.

Isso é feito digitando este comando na visualização de comandos:

terminal digite :

    python manage.py createsuperuser

O que dará este prompt:

Aqui você deve digitar:

    nome de usuário 
    endereço de e-mail (você pode escolher um endereço de e-mail falso) 
    senha:

    Username: sandeison
    Email address: sandeisonfernandes@gmail.com
    Password: 123456789
    Password (again): 123456789
    Esta senha é muito curta. Ela deve conter pelo menos 8 caracteres.
    Esta senha é muito comum.
    Esta senha é totalmente numérica.
    Ignorar a validação de senha e criar usuário mesmo assim? [s/N]:

Minha senha não atendeu aos critérios, mas este é um ambiente de teste e escolhi criar um usuário mesmo assim, digitando y:
    
    Bypass password validation and create user anyway? [y/N]: y

Se você pressionar [Enter], deverá ter criado um usuário com sucesso:

    Superuser created successfully.

Agora inicie o servidor novamente:

No terminal digite :

    python manage.py runserver

Na janela do navegador, digite 127.0.0.1:8000/admin/na barra de endereço.

Agora é preencha o formulário com o nome de usuário e senha corretos para acessar o sisitema.


1.3  Incluir modelos no Django Admin 

Para incluir o modelo Member na interface de administração, temos que informar ao Django que esse modelo deve estar visível na interface de administração.

Isso é feito em um arquivo chamado admin.pye está localizado na pasta do seu aplicativo, que no nosso caso é a memberspasta .

Abra-o e ele deverá ficar assim:

    from django.contrib import admin  
    # Register your models here.

    admin.site.register(Post)



### 5. Tipos de dados no Django

*5.1 CharField*

Utilizado para textos curtos, como nomes ou títulos. É necessário definir o atributo max_length para o tamanho máximo. 


*5.2 TextField*

Semelhante ao CharField, mas para armazenar textos longos. 

*5.3 IntegerField*

Armazena números inteiros, podendo ser usado para validação e como base para campos auto-incrementáveis como o AutoField. 

*5.4 DateField*

Armazena valores de data, convertidos em objetos datetime.date. 

*5.5 DateTimeField*

Armazena data e hora, convertidas em objetos datetime.datetime. 

*5.6 EmailField*

Para armazenar e validar endereços de e-mail, com max_length padrão de 100. 

*5.7 AutoField*

Um tipo especial de IntegerField que incrementa automaticamente o valor, servindo como identificador único para os registros. 


5.8 Exemplo 

from django.db import models

class Pessoa(models.Model):

    # CharField - usado para strings curtas, precisa de max_length
    nome = models.CharField(max_length=100)

    # TextField - usado para textos longos
    biografia = models.TextField(blank=True, null=True)

    # IntegerField - números inteiros
    idade = models.IntegerField()

    # DateField - apenas data (sem hora)
    data_nascimento = models.DateField()

    # DateTimeField - data e hora
    criado_em = models.DateTimeField(auto_now_add=True)   # preenchido automaticamente na criação
    atualizado_em = models.DateTimeField(auto_now=True)   # atualizado sempre que salvar

    # EmailField - valida formato de e-mail automaticamente
    email = models.EmailField(unique=True)

    # AutoField - chave primária automática (geralmente Django já cria sozinho o "id")
    codigo = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.nome} ({self.email})"


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