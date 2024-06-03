from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    title = 'Главная страница'
    return render(request, 'post/list.html', {"title": title})

def news(request):
    posts = Post.objects.all()
    title = 'Новости'
    return render(request, 'post/list.html', {"posts": posts, "title": title})

def detail(request, pk):
    posts = Post.objects.all()
    post = posts.get(pk=pk)
    title = post.title

    first = posts.first().id
    last = posts.last().id
    count = str(request.GET.get("post_page"))

    return render(request, 'post/post_detail.html', {"post": post, "title": title})
