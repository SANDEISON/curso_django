# 📘 Curso de Django com Python

## 🔹 Aula 2 – Configuração do ambiente de desenvolvimento

Nesta aula, vamos preparar o computador para desenvolver aplicações com Python e Django. Ao final, teremos um ambiente virtual isolado e os arquivos iniciais necessários para controlar as dependências do projeto.

> **Observação:** este guia apresenta os comandos para Windows utilizando PowerShell ou Prompt de Comando (CMD).

## 🎯 Objetivos da aula

Ao final desta aula, você será capaz de:

- instalar e verificar o Python;
- escolher um editor de código;
- compreender a função do `pip`;
- criar, ativar e desativar um ambiente virtual;
- configurar um arquivo `.gitignore`;
- criar e utilizar um arquivo `requirements.txt`.

## 📍 Pré-requisitos

Antes de começar, é recomendável ter:

- acesso de administrador para instalar programas;
- conexão com a internet;
- conhecimentos básicos sobre arquivos, pastas e terminal;
- Git instalado, caso acompanhe o curso pelas branches do repositório.

## 1. Instalação do Python

### 1.1 Baixe o instalador

Acesse a [página oficial de downloads do Python](https://www.python.org/downloads/) e baixe o instalador indicado para Windows.

### 1.2 Execute e configure a instalação

1. Localize o instalador, normalmente salvo na pasta `Downloads`.
2. Clique duas vezes no arquivo para executá-lo.
3. Na primeira tela, marque a opção **Add python.exe to PATH**.
4. Clique em **Install Now**.
5. Ao final, clique em **Disable path length limit**, caso essa opção seja exibida.

A opção **Add python.exe to PATH** permite executar o Python diretamente pelo terminal.

### 1.3 Verifique a instalação

Abra um novo PowerShell ou Prompt de Comando e execute:

```powershell
python --version
```

Se o comando `python` não for reconhecido, tente utilizar o inicializador do Python para Windows:

```powershell
py --version
```

O terminal deverá apresentar uma versão no formato `Python 3.x.x`.

## 2. Escolha do editor de código

Você pode acompanhar o curso utilizando o editor ou a IDE de sua preferência. Duas opções populares são:

- [Visual Studio Code](https://code.visualstudio.com/);
- [PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/?section=windows).

Se utilizar o Visual Studio Code, instale também a extensão oficial **Python**, publicada pela Microsoft.

## 3. Criação do ambiente virtual

Um ambiente virtual isola as bibliotecas utilizadas por cada projeto. Isso evita conflitos entre versões instaladas em projetos diferentes.

### 3.1 Abra a pasta do projeto

Crie ou selecione a pasta na qual o projeto será desenvolvido e abra um terminal nessa pasta.

### 3.2 Crie o ambiente virtual

Execute:

```powershell
python -m venv .venv
```

Se estiver utilizando o inicializador `py`, execute:

```powershell
py -m venv .venv
```

O comando criará a pasta `.venv`, que armazenará uma instalação isolada do Python e as dependências do projeto.

### 3.3 Ative o ambiente virtual

No PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Prompt de Comando (CMD):

```bat
.venv\Scripts\activate.bat
```

Depois da ativação, o terminal deverá exibir `(.venv)` antes do caminho atual:

```text
(.venv) PS C:\caminho\do\projeto>
```

### 3.4 Se o PowerShell bloquear a ativação

Caso o PowerShell informe que a execução de scripts foi desabilitada, libere-a apenas para a sessão atual:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Em seguida, execute novamente:

```powershell
.\.venv\Scripts\Activate.ps1
```

A opção `Process` limita a alteração ao terminal aberto. A configuração é descartada quando ele é fechado.

### 3.5 Desative o ambiente virtual

Quando terminar de trabalhar no projeto, execute:

```powershell
deactivate
```

## 4. Gerenciamento de pacotes com `pip`

O `pip` é o gerenciador de pacotes do Python. Ele permite instalar e atualizar bibliotecas, incluindo o Django.

Com o ambiente virtual ativo, verifique se o `pip` está disponível:

```powershell
python -m pip --version
```

Utilizar `python -m pip` ajuda a garantir que o pacote seja instalado no ambiente Python atualmente selecionado.

> Nesta aula ainda não instalaremos o Django. Essa instalação será realizada na próxima etapa do curso.

## 5. Configuração do `.gitignore`

O `.gitignore` informa ao Git quais arquivos e pastas não devem ser versionados.

Ele é importante para:

- impedir o versionamento do ambiente virtual e de arquivos temporários;
- reduzir arquivos desnecessários no repositório;
- evitar o envio acidental de credenciais e configurações locais;
- diminuir conflitos entre ambientes de desenvolvimento.

Crie o arquivo `.gitignore` na raiz do projeto. Para este curso, ele deve incluir pelo menos:

```gitignore
# Ambiente virtual
.venv/
venv/

# Cache do Python
__pycache__/
*.py[cod]

# Variáveis de ambiente e configurações locais
.env

# Editores e IDEs
.idea/
.vscode/

# Arquivos locais do Django
db.sqlite3
*.log
```

Uma lista mais completa pode ser gerada em [gitignore.io](https://www.toptal.com/developers/gitignore), selecionando os modelos para Python, Django e o editor utilizado.

> O `.gitignore` não remove automaticamente arquivos que já foram adicionados ao histórico do Git.

## 6. Uso do `requirements.txt`

O arquivo `requirements.txt` registra as bibliotecas necessárias para executar o projeto. Ele ajuda a reproduzir o mesmo ambiente em outro computador.

### 6.1 Registre as dependências instaladas

Depois de instalar as bibliotecas do projeto, execute:

```powershell
python -m pip freeze > requirements.txt
```

Neste momento do curso, o arquivo permanecerá vazio porque ainda não instalamos nenhuma dependência no ambiente virtual.

### 6.2 Instale dependências existentes

Ao clonar um projeto que já possui dependências registradas, ative o ambiente virtual e execute:

```powershell
python -m pip install -r requirements.txt
```

## ✅ Checklist da aula

Antes de avançar, confirme se:

- [ ] o comando `python --version` ou `py --version` exibe a versão instalada;
- [ ] a pasta `.venv` foi criada;
- [ ] o terminal exibe `(.venv)` quando o ambiente está ativo;
- [ ] o comando `python -m pip --version` funciona;
- [ ] a pasta `.venv` está incluída no `.gitignore`;
- [ ] o arquivo `requirements.txt` existe na raiz do projeto.

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
