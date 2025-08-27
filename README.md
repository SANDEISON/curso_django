# 📘Curso de Django (Python)

Este repositório apresenta um guia detalhado para a instalação e criação de um projeto Django.

Ao longo do material, será desenvolvida uma aplicação capaz de realizar as operações de criação, leitura, atualização e exclusão de dados (CRUD).
Serão abordados tópicos como a criação de templates HTML, o uso das tags de template do Django para inserção dinâmica de dados, bem como o trabalho com QuerySets para consulta, filtragem e ordenação de informações.

Também será demonstrado o processo de configuração do banco de dados PostgreSQL e as etapas necessárias para a implantação do projeto em produção.

Para seguir este guia você pode acessar as branches criadas para cada Aula.


## 🔹 Aula 1 – Introdução ao Django

## 📍 O que é Django?

#### 1. História e Propósito do Django

Origem: Criado em 2003 por desenvolvedores de um jornal online, com a necessidade de construir aplicações web rápidas e seguras.

Lançamento oficial: 2005, como projeto de código aberto.

Nome: Uma homenagem ao guitarrista de jazz Django Reinhardt.

Propósito: Facilitar o desenvolvimento rápido de aplicações web robustas e escaláveis, com foco em produtividade, segurança e escalabilidade.

Diferenciais:

Já vem com recursos prontos como autenticação, administração, ORM, sistema de templates etc.

Comunidade ativa e ampla documentação.

Framework maduro e usado por empresas como Instagram, Pinterest, Disqus e Spotify.


#### 2. Diferença entre Frameworks Web (Flask x Django)

| Aspecto	            |      Flask (Microframework)      | Django (Framework Completo) |
|:---------------------|:--------------------------------:|----------------------------:|
| Tamanho              | Minimalista, apenas o essencial  |                Completo, inclui ORM, autenticação, admin etc.   |
| Flexibilidade        |                Mais liberdade para escolher bibliotecas externas                |                    Estrutura rígida, mas padronizada |
| Curva de aprendizado |                Mais simples no início                |                     Mais robusto, exige aprendizado da arquitetura MVT |
| Casos de uso |                APIs pequenas, microsserviços, protótipos rápidos                |                     Sistemas completos, grandes portais e e-commerces |
| Filosofia |                “Escolha o que usar”                |                     “Pronto para uso” |

Resumo:

Flask é indicado para projetos menores, onde o desenvolvedor deseja total controle.

Django é ideal para projetos médios e grandes, que precisam de rapidez no desenvolvimento e boas práticas já embutidas.


#### 3. Arquitetura MVT (Model–View–Template)

O Django utiliza o padrão MVT, que é uma variação do famoso MVC.

**Model (Modelo)**

   Responsável pela camada de dados.

   Define tabelas do banco de dados usando classes Python.

   Trabalha com o ORM (Object-Relational Mapping) do Django.

   Exemplo: class Produto(models.Model): nome = models.CharField(max_length=100)

**View (Visão)**

   Lida com a lógica de negócio.

   Recebe requisições, processa dados (via modelos) e retorna uma resposta.

   Exemplo: def home(request): return render(request, "index.html")

**Template (Modelo de Apresentação)**

   Responsável pela interface com o usuário.

   Usa a linguagem de templates do Django (HTML + tags dinâmicas).

   Exemplo: < h1>{{ produto.nome }} < /h1>


📌 Fluxo resumido de uma requisição no Django:

Usuário acessa uma URL.

O View correspondente é acionado.

O View interage com o Model (se necessário).

O View retorna uma resposta renderizada com o Template.

### Cronograma das Aulas 

| Aula	                                             | Branch |                                                Clique no Link |
|:--------------------------------------------------|:------:|--------------------------------------------------------------:|
| Aula 1 – O que é Django?                          | aula_1 | [Link](https://github.com/SANDEISON/curso_django)  |
| Aula 2 - Configuração do Ambiente Django          | aula_2 | [Link](https://github.com/SANDEISON/curso_django/tree/aula_2) |
| Aula 3 - Criação e Estrutura do Projeto em Django | aula_3 | [Link](https://github.com/SANDEISON/curso_django/tree/aula_3) |
| Aula 4                                            |        |                                                               |
| Aula 5                                            |        |                                                               |

