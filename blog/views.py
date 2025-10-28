from django.shortcuts import render, redirect, get_object_or_404

from blog.forms import PostForm
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


def post_list(request):
    posts = Post.objects.all().order_by('-data_criacao')
    return render(request, 'post_list.html', {'posts': posts})



def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('post_list')

    return render(request, 'post_edit.html', {'form': form})
