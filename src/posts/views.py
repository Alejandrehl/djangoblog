from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from posts.models import Post

# Create your views here.
def post_create(request):
    return HttpResponse("<h1>Create post</h1>")

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        "titulo" : post.titulo,
        "post" : post 
    }
    return render(request, "post_detail.html", context)

def post_delete(request):
    return HttpResponse("<h1>Delete post</h1>")

def post_update(request):
    return HttpResponse("<h1>Update post</h1>")

def post_list(request):
    posts = Post.objects.all()
    context = {
        "titulo" : "Artículos",
        "posts" : posts 
    }
    return render(request, "index.html", context)
