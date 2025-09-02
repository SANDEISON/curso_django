from django.http import HttpResponse
from django.template import loader
from blog.models import Post
# Create your views here.
def home(request):
    posts = Post.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))
