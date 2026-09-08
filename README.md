# 📘 Curso de Django com Python

Este repositório contém o material prático de um curso introdutório de desenvolvimento web com Django.

O curso é indicado para estudantes que já possuem conhecimentos básicos de Python e desejam aprender a desenvolver aplicações web completas, organizadas e conectadas a um banco de dados.

Ao longo das aulas, será desenvolvida uma aplicação capaz de realizar operações de criação, leitura, atualização e exclusão de dados (CRUD). O material também apresenta templates HTML, tags de template, QuerySets, PostgreSQL, APIs e autenticação.

## 🎯 O que você aprenderá

Ao final do curso, você será capaz de:

- configurar um ambiente de desenvolvimento Django;
- criar e organizar projetos e aplicações;
- trabalhar com URLs, views e templates;
- modelar, consultar, filtrar e ordenar dados utilizando o ORM;
- implementar operações de CRUD;
- utilizar o painel administrativo do Django;
- criar views baseadas em função e em classe;
- desenvolver APIs com Django REST Framework;
- implementar autenticação com Token e JWT.

## 🛠️ Pré-requisitos

Para acompanhar o curso, é recomendável possuir:

- conhecimentos básicos de Python;
- noções básicas de HTML;
- familiaridade com terminal ou prompt de comando;
- Python e Git instalados no computador.

Não é necessário ter experiência anterior com Django.

## 📂 Como acompanhar as aulas

Cada aula possuirá uma branch correspondente, como `aula_1`, `aula_2` e `aula_3`. Assim, será possível consultar o estado do projeto em cada etapa do curso.

Depois de clonar o repositório, utilize o comando abaixo para acessar a branch de uma aula:

```bash
git switch aula_2
```

> **Observação:** as branches e seus respectivos conteúdos serão atualizados conforme o andamento das aulas.

## 🗓️ Cronograma das aulas

| Aula                                                   | Branch  | Acesso                                                         |
|:-------------------------------------------------------|:-------:|:---------------------------------------------------------------|
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

## 🔹 Aula 1 – Introdução ao Django

### 📍 O que é Django?

Django é um framework web de alto nível escrito em Python. Ele oferece uma estrutura organizada e diversos recursos prontos para acelerar a criação de aplicações seguras, escaláveis e de fácil manutenção.

### 1. História e propósito do Django

- **Origem:** criado em 2003 por desenvolvedores de um jornal on-line que precisavam construir aplicações web com rapidez.
- **Lançamento oficial:** disponibilizado como projeto de código aberto em 2005.
- **Nome:** homenagem ao guitarrista de jazz Django Reinhardt.
- **Propósito:** facilitar o desenvolvimento rápido de aplicações web, com foco em produtividade, segurança e escalabilidade.

Entre os principais diferenciais do Django estão:

- sistema de autenticação;
- painel administrativo;
- ORM para interação com bancos de dados;
- sistema de templates;
- recursos de segurança;
- comunidade ativa e ampla documentação.

### 2. Diferenças entre frameworks web: Flask e Django

| Aspecto | Flask (microframework) | Django (framework completo) |
|:---|:---|:---|
| Estrutura | Minimalista, fornece os recursos essenciais | Completa, inclui ORM, autenticação e painel administrativo |
| Flexibilidade | Oferece mais liberdade para escolher bibliotecas externas | Possui uma estrutura mais opinativa e padronizada |
| Aprendizado | Possui menos conceitos iniciais | Exige o aprendizado de uma arquitetura mais abrangente |
| Casos de uso | APIs pequenas, microsserviços e protótipos | Sistemas completos, portais e comércios eletrônicos |
| Filosofia | Escolha as ferramentas de que precisa | Muitos recursos disponíveis desde o início |

Flask oferece maior liberdade na escolha dos componentes do projeto. Django fornece uma estrutura mais completa e padronizada. A escolha depende das necessidades, da equipe e do tamanho de cada aplicação.

### 3. Arquitetura MVT (Model–View–Template)

O Django utiliza a arquitetura MVT, uma variação do padrão MVC. Nela, cada componente possui uma responsabilidade específica.

#### Model (modelo)

Representa e gerencia os dados da aplicação. Os models definem as tabelas do banco de dados por meio de classes Python e utilizam o ORM (*Object-Relational Mapping*) do Django.

```python
class Produto(models.Model):
    nome = models.CharField(max_length=100)
```

#### View (visão)

Recebe uma requisição, executa a lógica necessária e retorna uma resposta. Na comparação com o MVC tradicional, a view do Django desempenha parte do papel normalmente associado ao controller.

```python
def home(request):
    return render(request, "index.html")
```

#### Template (apresentação)

Define a interface exibida ao usuário. Utiliza HTML combinado com variáveis, filtros e tags da linguagem de templates do Django.

```html
<h1>{{ produto.nome }}</h1>
```

### 📌 Fluxo resumido de uma requisição

1. O usuário acessa uma URL.
2. O Django localiza a view associada a essa URL.
3. A view interage com o model, quando necessário.
4. A view processa os dados e pode renderizar um template.
5. O Django envia a resposta ao navegador do usuário.
