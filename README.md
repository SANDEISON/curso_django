# 📘Curso de Django (Python)

## 🔹 Aula 2 – Configuração do Ambiente Django

## 📍 Pré-requisitos

### 1. Instalação do Python

Essa instalação é baseada no sisitema operacional windows

1.1 Acesse ao site oficial:

Acesse o site [python.org/downloads](https://www.python.org/downloads/) 

**1.2 Faça o download do instalador:**

Clique em download na versão mais recente do Python. 

**1.3 Execute o instalador:**

Localize o arquivo (normalmente na pasta "Downloads") e clique duas vezes nele para iniciar o processo de instalação.

**1.4 Configure a instalação:**

No tela inicial do instalador, é crucial marcar a opção "Add python.exe to PATH". Isto permite que execute comandos Python diretamente no terminal. 

**1.5 Inicie a instalação:**

Clique em "Install Now" (ou "Instalar Agora") para começar a instalação com as configurações padrão. 

**1.6 Conclua a instalação:**

Aguarde enquanto o instalador completa a instalação do Python. Na tela final, pode aparecer uma opção para "Disable path length limit", que é recomendado que clique. 

**1.7 Verifique a instalação:**

Para confirmar se tudo foi instalado corretamente, abra o Prompt de Comando (CMD) ou o PowerShell e digite o comando python --version. 

**1.8 Confirme o resultado:**

Se a instalação foi bem-sucedida, o terminal irá apresentar a versão do Python que foi instalada, como Python 3.x.x

Caso tenha algum problema refaça os passos anteriores. 



**Editor de código**

[Visual Studio Code](https://code.visualstudio.com/)

[PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/?section=windows)

**PIP**

É um gerenciador de pacotes do Python, já vem junto com as versões recentes do Python.

Git (opcional, mas útil para versionamento).

### 2. Criação de um Ambiente Virtual

O ambiente virtual serve para isolar as dependências de cada projeto.

2.1 Abra um editor de código de sua preferencia

2.2 Selecione a pasta onde ira salvar seus projetos

2.3 Abra o terminal

2.4 Crie o ambiente virtual digitando o comando no terminal: 

- python -m venv venv

2.5 Ative o ambiente virtual:
- venv\Scripts\activate

2.6 Confirme que o ambiente está ativo (o terminal exibirá (venv) antes do caminho).

Ex: (venv) PS D:\Sandeison\Documents\


### 3. Por que o .gitignore é importante?

**Manter repositórios limpos:**

Evita que arquivos temporários, logs e outros itens que não são parte do código-fonte se tornem parte do histórico do projeto. 

**Evitar vazamento de informações confidenciais:**

Ajuda a impedir o envio acidental de chaves de API, credenciais e outras informações sensíveis para o repositório. 

**Simplificar a colaboração:**

Ao manter os commits focados no código relevante, a colaboração entre desenvolvedores se torna mais eficiente e menos suscetível a conflitos por arquivos indesejados. 

**Otimizar o controle de versão:**

Reduz o tamanho e o ruído dos repositórios, tornando mais rápida a clonagem, o download e outras operações com o Git. 



3.1 Gerar arquivos para o git ignore

Link para gerar uma lista de nomes de arquivos para serem ignorados dependendo da linguagem de programação.

[toptal](https://www.toptal.com/developers/gitignore)

3.2 Crie um arquivo .gitignore dentro do repositorio

- Um exemplo pode ser visto dentro deste repositorio.


### 4. Importancia do arquivo requeriments.txt no django

O requirements.txt no Django (e em projetos Python em geral) 
é fundamental porque lista todas as dependências do projeto e suas versões exatas, 
garantindo que o ambiente de desenvolvimento e produção possa ser reproduzido com exatidão por 
qualquer membro da equipe, em qualquer sistema. Isso evita problemas de compatibilidade, 
como o temido "funciona na minha máquina", facilita a colaboração, a automação de deploys e o 
controle de versões das bibliotecas.

4.1 Criação:
- Abra o terminal e digite : pip freeze > requirements.txt

    Sera gerado um arquivo no seu projeto requirements.txt

4.2 Instalação:

Caso você esteja em outra maquina e baixe o projeto.

Primeiro você tem que criar o ambiente virtual, siga o passo 2. Criação de um Ambiente Virtual.

Depois no termial você digita : 
- pip install -r requirements.txt

Ate o momento não instalamos nenhuma dependência no projeto, então o arquivo gerado vai estar vazio.


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
