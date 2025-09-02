# 📘Curso de Django (Python)

## 🔹 Aula 6 – Exibindo dados do Models no Template

### 1. Variáveis 

Em modelos Django, você pode renderizar variáveis
colocando-as entre {{ }} colchetes:

Exemplo: 

    <h1>Hello {{ firstname }}, how are you?</h1>

A variável firstname foi criado na view, vamos ver mais a diante essa implementação.


### 2. Criar variáveis

A variável firstname no exemplo acima foi enviada ao modelo por meio de uma visualização:

    views.py:
        from django.http import HttpResponse
        from django.template import loader
        
        def testing(request):
          template = loader.get_template('template.html')
          context = {
            'firstname': 'Linus',
          }
          return HttpResponse(template.render(context, request))


Como você pode ver na visão acima, criamos um objeto chamado context, 
o preenchemos com dados e o enviamos como o primeiro parâmetro na template.render() da função.



### 3.Obtendo Dados de um modelo

O exemplo acima mostrou uma abordagem fácil sobre como criar e usar variáveis em um modelo.

Normalmente, a maioria dos dados externos que você deseja usar vem de um modelo.

Na aula 5 criamos um modelo chamado Post.
Para obter dados do modelo, teremos que importá-los no arquivo views.py e extrair os dados dele na visualização:

    views.py
    from django.http import HttpResponse, HttpResponseRedirect
    from django.template import loader
    from .models import Member

    def testing(request):
      posts = Post.objects.all().values()
      template = loader.get_template('home.html')
      context = {
        'posts': posts,
      }
      return HttpResponse(template.render(context, request))

Agora podemos usar os dados do modelo na pagina home.html:


    templates/home.html:

    {% extends "base.html" %}
    {% block content %}     
      <ul>
        {% for i in posts %}
          <li>{{ i.titulo }}</li>
        {% endfor %}
      </ul>    
    {% endblock %}


Usamos a tag de modelo do Django {% for %} para percorrer os posts.



### 4. Tags de modelo Django

Nos modelos do Django, você pode executar lógica de programação, como executar ifinstruções e forloops.

Essas palavras-chave, ife for, são chamadas de "tags de modelo" no Django.

Para executar tags de modelo, nós as colocamos entre {% %}colchetes.

Exemplos:

    {% if aprovado == 1 %}
      <h1>Hello</h1>
    {% else %}
      <h1>Bye</h1>
    {% endif %}

As tags de modelo são uma maneira de dizer ao Django que aqui vem algo diferente de HTML simples.

As tags de modelo nos permitem fazer alguma programação no servidor antes de enviar o HTML para o cliente.


*4.1 Tag if*

    {% if verdadeiro == 1 %}
      <h1>Hello</h1>
    {% endif %} 

*4.2 Tag elif * 

    {% if perfil == 1 %}
      <h1>Hello</h1>
    {% elif perfil == 2 %}
      <h1>Welcome</h1>
    {% endif %} 

*4.3 Tag else*

    {% if aprovado == 1 %}
      <h1>Aprovado</h1>
    {% elif aprovado == 2 %}
      <h1>Reavaliação</h1>
    {% else %}
      <h1>Reprovado</h1>
    {% endif %} 





### 5. Operadores

Os exemplos acima usam o operador ==, que é usado para verificar se uma variável é igual a um valor, mas há muitos outros operadores que você pode usar, ou você pode até mesmo descartar o operador se quiser apenas verificar se uma variável não está vazia:

Exemplos: 

    {% if verdadeiro %}
      <h1>Hello</h1>
    {% endif %} 


*5.1 Operador == , Igual*

    {% if verdadeiro == 1 %}
      <h1>Hello</h1>
    {% endif %} 

*5.2 Operador != , Não é igual a*

    {% if verdadeiro != 1 %}
      <h1>Hello</h1>
    {% endif %} 


*5.3 Operador < , É menor que*

    {% if valor < 5 %}
      <h1>Hello</h1>
    {% endif %} 

*5.4 Operador <= , É menor ou igual a*

    {% if valor <= 5 %}
      <h1>Hello</h1>
    {% endif %} 

*5.5 Operador > , É maior que*

    {% if valor > 5 %}
      <h1>Hello</h1>
    {% endif %} 

*5.6 Operador >= ,É maior ou igual a*

    {% if valor >= 5 %}
      <h1>Hello</h1>
    {% endif %} 

*5.7 Operador e *

Para verificar se mais de uma condição é verdadeira.

    {% if aprovado == 1 and faltas < 10  %}
      <h1>Hello</h1>
    {% endif %} 

*5.8 Operador ou *

Para verificar se uma das condições é verdadeira.

    {% if aprovado == 2 or  media < 7  %}
      <h1>Reprovado</h1>
    {% endif %} 


*5.9 Operador e/ou *

Combine and e or.

    {% if id_user == 10 and senha == "123456" or idade > 18  %}
      <h1>Bem vindo</h1>
    {% endif %} 

*5.10 Operador em *

Para verificar se um determinado item está presente em um objeto.

    {% if 'Banana' in fruits %}
      <h1>Hello</h1>
    {% else %}
      <h1>Goodbye</h1>
    {% endif %} 

*5.11 Operador não em *

Para verificar se um determinado item não está presente em um objeto.

    {% if 'Banana' not in fruits %}
      <h1>Hello</h1>
    {% else %}
      <h1>Goodbye</h1>
    {% endif %} 

### 5. Loop for

Um forloop é usado para iterar sobre uma sequência, como fazer um loop sobre itens em uma matriz, uma lista ou um dicionário.

    {% for x in fruits %}
      <h1>{{ x }}</h1>
    {% endfor %}
