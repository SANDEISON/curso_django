from django.shortcuts import render
from blog.models import Post
# Create your views here.
def login(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        senha = request.POST.get("senha")
        posts = Post.objects.all().values()
        print(nome)
        print(senha)
        return render(request, 'home.html', locals())

    return render(request, 'login.html', locals())
