# 📘Curso de Django (Python)

## 🔹 Aula 9 – Explorando o Painel Administrativo do Django

O Django Admin é uma interface web automática que o Django fornece para gerenciar os dados do seu projeto. 

Ele permite:

Criar, ler, atualizar e deletar registros (CRUD).

Pesquisar e filtrar dados.

Configurar visualizações customizadas para modelos específicos.

Vantagens:

Ganha-se rapidez no desenvolvimento.

Não precisa criar interfaces básicas de administração do zero.

Totalmente integrado com o ORM do Django.



### 1. Configuração Inicial do Admin

1.1 Certifique-se de que o app está registrado no INSTALLED_APPS:
       
     # settings.py
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'accounts',  # nosso app de exemplo
    ]

1.2 Crie um superusuário para acessar o admin:
    
    python manage.py createsuperuser


1.3 Execute o servidor:

    python manage.py runserver

1.4 Acesse o admin em http://127.0.0.1:8000/admin/

### 2. Registrando Modelos no Admin
    
Para que um modelo apareça no painel administrativo, é necessário registrá-lo.

Exemplo com modelo Pessoa:

    # accounts/models.py
    from django.db import models
    
    class Pessoa(models.Model):
        nome = models.CharField(max_length=100)
        email = models.EmailField()
        idade = models.IntegerField()
    
        def __str__(self):
            return self.nome

Registrar no admin:

    # accounts/admin.py
    from django.contrib import admin
    from .models import Pessoa
    
    @admin.register(Pessoa)
    class PessoaAdmin(admin.ModelAdmin):
        list_display = ('nome', 'email', 'idade')
        search_fields = ('nome', 'email')
        list_filter = ('idade',)

Explicações:

list_display → Colunas exibidas na lista do admin.

search_fields → Campos que podem ser pesquisados.

list_filter → Filtros laterais para agilizar consultas.



### 3. Personalizando o Admin

O Django Admin permite customizações avançadas:

3.1 Agrupando campos com fieldsets

    @admin.register(Pessoa)
    class PessoaAdmin(admin.ModelAdmin):
        fieldsets = (
            ('Informações Pessoais', {'fields': ('nome', 'rg')}),
            ('Contato', {'fields': ('telefone',)}),
        )

3.2 Tornando campos editáveis diretamente na lista

    @admin.register(Pessoa)
    class PessoaAdmin(admin.ModelAdmin):
        list_display = ('user', 'cpf', 'data_nascimento')
        list_editable = ('idade',)


3.3 Tornando determinados campos visíveis, mas não editáveis

    @admin.register(Pessoa)
    class PessoaAdmin(admin.ModelAdmin):
        list_display = ('nome', 'email', 'idade', 'data_criacao')
        readonly_fields = ('data_criacao',)

3.4 Exibir e editar objetos relacionados

Inlines são classes auxiliares que permitem exibir e editar objetos relacionados (via ForeignKey ou OneToOneField) dentro do formulário de outro modelo no painel administrativo do Django.

Em outras palavras:

Quando um modelo tem uma relação com outro, você pode mostrar e editar esses objetos filhos dentro da página do objeto pai no admin.

Quando usar

Você usa inlines quando deseja:

Gerenciar dados relacionados sem sair da tela principal.

Evitar múltiplos acessos e formulários separados.

Criar uma experiência mais fluida para o administrador.

Por exemplo:

Uma Pessoa pode ter vários Endereços → editar todos os endereços direto na tela da pessoa.

Um Pedido pode ter vários Itens → editar todos os itens dentro do pedido.


Exemplo:

Modelos

    # accounts/models.py
    from django.db import models
    
    class Pessoa(models.Model):
        nome = models.CharField(max_length=100)
        email = models.EmailField()
    
        def __str__(self):
            return self.nome
    
    class Endereco(models.Model):
        pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
        rua = models.CharField(max_length=100)
        numero = models.CharField(max_length=10)
        cidade = models.CharField(max_length=50)
    
        def __str__(self):
            return f"{self.rua}, {self.numero} - {self.cidade}"

Admin com Inline
    
    # accounts/admin.py
    from django.contrib import admin
    from .models import Pessoa, Endereco
    
    # Define o inline (modelo filho)
    class EnderecoInline(admin.TabularInline):  # ou admin.StackedInline
        model = Endereco
        extra = 1  # número de formulários vazios exibidos
    
    # Modelo principal com inline
    @admin.register(Pessoa)
    class PessoaAdmin(admin.ModelAdmin):
        list_display = ('nome', 'email')
        inlines = [EnderecoInline]

Tipos de Inline

admin.TabularInline
➜ Exibe os campos em tabela (mais compacto).

admin.StackedInline
➜ Exibe os campos em blocos verticalizados, como formulários normais.

Exemplo de uso:

    class EnderecoInline(admin.StackedInline):
        model = Endereco



Parâmetros Úteis

| Parâmetro         | Descrição                                                |
| ----------------- | -------------------------------------------------------- |
| `model`           | Modelo relacionado que será exibido no inline            |
| `extra`           | Quantos formulários vazios aparecem para novos registros |
| `max_num`         | Número máximo de objetos que podem ser criados           |
| `readonly_fields` | Campos apenas leitura dentro do inline                   |
| `can_delete`      | Permite ou bloqueia exclusão de registros no inline      |


O atributo inlines permite incluir modelos relacionados dentro da interface do admin de um modelo principal, oferecendo edição rápida, integrada e intuitiva dos relacionamentos.


3.5 Executar operações personalizadas em lote

Quando usar

- Você usa actions quando precisa realizar operações repetitivas ou automatizadas diretamente no admin, como:

- Atualizar o status de vários registros.

- Enviar notificações ou e-mails em massa.

- Excluir, duplicar ou exportar dados.

- Aplicar transformações em campos de vários objetos ao mesmo tempo.

Exemplo prático

Modelo

    # accounts/models.py
    from django.db import models
    
    class Pessoa(models.Model):
        nome = models.CharField(max_length=100)
        email = models.EmailField()
        idade = models.IntegerField()
    
        def __str__(self):
            return self.nome

Admin com ação personalizada

    # accounts/admin.py
    from django.contrib import admin
    from .models import Pessoa
    
    @admin.register(Pessoa)
    class PessoaAdmin(admin.ModelAdmin):
        list_display = ('nome', 'email', 'idade')
        actions = ['envelhecer_uma_vez']
    
        def envelhecer_uma_vez(self, request, queryset):
            for pessoa in queryset:
                pessoa.idade += 1
                pessoa.save()
            self.message_user(request, "As pessoas selecionadas envelheceram um ano! ")
    
        envelhecer_uma_vez.short_description = "Envelhecer pessoas selecionadas"


Como funciona no Django Admin

- O administrador acessa a lista de pessoas.

- Marca várias pessoas usando as caixas de seleção.

- No menu suspenso “Ações”, escolhe “Envelhecer pessoas selecionadas”.

- Ao clicar em “Executar”, a ação é aplicada a todos os registros marcados.



### 4. Recursos Visuais (Resumo)


| Recurso           | Descrição                           |
| ----------------- | ----------------------------------- |
| `list_display`    | Define colunas visíveis na listagem |
| `search_fields`   | Permite pesquisa rápida             |
| `list_filter`     | Filtros laterais                    |
| `list_editable`   | Edição direta de campos             |
| `readonly_fields` | Campos somente leitura              |
| `inlines`         | Edição de modelos relacionados      |
| `actions`         | Cria ações personalizadas           |
| `fieldsets`       | Agrupa campos no formulário         |


### Dicas de Boas Práticas

Use @admin.register(Modelo) para registrar diretamente.

Sempre defina __str__ nos modelos — isso melhora a visualização.

Limite o número de campos em list_display (para evitar poluição visual).

Utilize filtros e buscas para facilitar a gestão de grandes volumes de dados.


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