from django.contrib.auth.models import User
from django.shortcuts import render
from blog.models import Post, Pessoa


# Create your views here.
def login(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        senha = request.POST.get("senha")
        lista_pessoas = []
        pessoas = Pessoa.objects.all().values()
        print(pessoas)
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
        return render(request, 'home.html', locals())

    return render(request, 'login.html', locals())