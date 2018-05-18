from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from posts.models import Post
from .forms import PostForm

# Create your views here.
def post_create(request):
    form = PostForm()

    if form.is_valid():
        instance = form.save(commit=false)
        instance.save()

    context = {
        "form" : form
    }
    return render(request, "post_form.html", context)

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
