# 📘Curso de Django (Python)

## 🔹 Aula 8 – Relacionamentos no Django

Em bancos de dados relacionais (como PostgreSQL, MySQL, SQLite), os relacionamentos permitem conectar tabelas entre si.

No Django, isso se reflete nos Models, que representam tabelas.

Assim, quando você quer dizer que:

Uma Pessoa tem vários Endereços,

Um Pedido pertence a um Cliente,

Um Aluno pode estar em várias Turmas,

➡️ Você usa os campos de relacionamento que o Django fornece.



### 1. O que é o ORM do Django?

1.1 O que é o ORM do Django?

ORM (Object-Relational Mapper) é uma camada que faz a “ponte” entre o banco de dados relacional (tabelas, colunas, SQL) e o mundo orientado a objetos do Python (classes, atributos, métodos).

No Django, você não precisa escrever SQL puro para manipular o banco de dados.
Em vez disso, você trabalha com classes (Models) e o ORM traduz automaticamente essas operações em queries SQL.

1.2 Como funciona?

- Você define suas tabelas como models (classes Python).

- O Django converte isso em tabelas no banco.

- Você interage com essas tabelas usando objetos, e o ORM cuida do SQL.


### 2. Tipos de Relacionamentos no Django


**2.1 One-to-One (Um para Um)**

Um registro está ligado a exatamente um outro registro.

📌 Exemplo: cada usuário do sistema tem apenas um perfil.

    from django.db import models
    from django.contrib.auth.models import User
    
    class Perfil(models.Model):
        usuario = models.OneToOneField(User, on_delete=models.CASCADE)
        data_nascimento = models.DateField()
        telefone = models.CharField(max_length=20)
    
        def __str__(self):
            return self.usuario.username



**2.2 ForeignKey (Um para Muitos)**

Um registro de uma tabela pode estar ligado a vários registros de outra.

📌 Exemplo: um cliente pode ter vários pedidos.

    class Cliente(models.Model):
        nome = models.CharField(max_length=100)
        email = models.EmailField()
    
        def __str__(self):
            return self.nome
    
    class Pedido(models.Model):
        cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
        data = models.DateTimeField(auto_now_add=True)
        total = models.DecimalField(max_digits=8, decimal_places=2)
    
        def __str__(self):
            return f"Pedido {self.id} - {self.cliente.nome}"



- Um Cliente pode ter vários Pedidos.
- Mas cada Pedido só pode estar ligado a um Cliente.

**2.3 Many-to-Many (Muitos para Muitos)**

Um registro pode estar relacionado a vários outros, e vice-versa.

📌 Exemplo: um aluno pode estar em várias turmas, e uma turma pode ter vários alunos.

    class Aluno(models.Model):
        nome = models.CharField(max_length=100)
    
        def __str__(self):
            return self.nome
    
    class Turma(models.Model):
        nome = models.CharField(max_length=50)
        alunos = models.ManyToManyField(Aluno)
    
        def __str__(self):
            return self.nome

-   Um Aluno pode estar em várias Turmas.

-   Uma Turma pode ter vários Alunos.

-   O Django cria uma tabela intermediária automaticamente.

2.4 Como funcionam os relacionamentos na prática?

Você pode acessar os dados de forma fácil com o ORM do Django:

    # Criando Cliente
    cliente = Cliente.objects.create(nome="João", email="joao@email.com")
    
    # Criando Pedido
    pedido1 = Pedido.objects.create(cliente=cliente, total=150.00)
    pedido2 = Pedido.objects.create(cliente=cliente, total=200.00)
    
    # Acessando pedidos de um cliente
    pedidos_cliente = cliente.pedido_set.all()   # retorna [pedido1, pedido2]
    
    # Acessando o cliente de um pedido
    print(pedido1.cliente.nome)  # João

Resumo:

-   OneToOneField → 1:1

-   ForeignKey → 1:N

-   ManyToManyField → N:N


2.4 Exemplo no projeto


No modelo Pessoa vamos adicionar o atributo usuário que vai receber o id do usuário do Django.

     class Pessoa(models.Model):
        usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario")
        nome = models.CharField(max_length=255, verbose_name=u'Nome')
        cpf = models.CharField(max_length=15, verbose_name=u'CPF')
        email = models.EmailField(verbose_name=u'Email')
        telefone = models.CharField(max_length=30, verbose_name=u'Telefone')
        data_nascimento = models.DateField(verbose_name=u'Data de nascimento')
        rg = models.CharField(max_length=30, verbose_name=u'RG', null=True, blank=True)
        endereco = models.CharField(max_length=255, verbose_name=u'Endereço residencial', null=True, blank=True)
        bairro = models.CharField(max_length=100, verbose_name=u'Bairro', null=True, blank=True)
    
    
        def __str__(self):
            return self.nome


No arquivo views.py obtemos os dados das pessoas cadastradas, e usuários de cada pessoa.

    from django.contrib.auth.models import User
    from django.http import HttpResponse
    from django.shortcuts import render
    
    from minhas_financas.models import Pessoa
    
    
    # Create your views here.

    def login(request):
        if request.method == "POST":
            nome = request.POST.get("nome")
            senha = request.POST.get("senha")
            lista_pessoas = []
            pessoas = Pessoa.objects.all().values()
            for i in pessoas:
                p_json = {}
                p_json['id'] = i['id']
                p_json['usuario_id'] = i['usuario_id']
                p_json['data_nascimento'] = i['data_nascimento']
                usuario = User.objects.get(id=i['usuario_id'])
                p_json['name_usuario'] = usuario.username
                p_json['primeir_nome_usuario'] = usuario.first_name
                p_json['email_usuario'] = usuario.email
                lista_pessoas.append(p_json)
    
    
            pessoas = lista_pessoas
    
            return render(request, 'minhas_financas/home.html', locals())
    
        return render(request, 'login.html', locals())


No arquivo home.html listamos as Pessoas cadastradas e usuários vinculados.

    {% extends "base.html" %}
    {% block content %}
      <ul>
        {% for i in pessoas %}
          <li> Usuario : {{ i.name_usuario }}</li>
          <li> Primeiro Nome : {{ i.primeir_nome_usuario }}</li>
          <li> Email : {{ i.email_usuario }}</li>
          <br/>
        {% endfor %}
      </ul>
    
    {% endblock %}


Obs: Antes de executar o projeto é necessário atualizar o banco de dados

Como estamos trabalhando com dados fictícios, vamos limpar todos os dados do banco.


Acesse a pasta de blog

- Exclua o arquivo db.sqlite3

No terminal digite:

    python manage.py makemigrations

No terminal digite :

    python manage.py migrate

É necessário criar o super usuário novamente.

No terminal digite :

    python manage.py createsuperuser