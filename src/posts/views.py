from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from posts.models import Post
from .forms import PostForm

# Create your views here.
# CREATE POST
def post_create(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Tu post ha sido creado correctamente :D")
        #return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form" : form
    }

    return render(request, "post_form.html", context)

# POST DETAIL
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        "titulo" : post.titulo,
        "contenido" : post.contenido,
        "post" : post 
    }
    return render(request, "post_detail.html", context)

# POST DELETE
def post_delete(request, id):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, 'Tu post ha sido borrado exitosamente.')
    return redirect("post_list")

# POST UPDATE
def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Tu post ha sido actualizado correctamente :D")
        #return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "titulo" : post.titulo,
        "contenido" : post.contenido,
        "form" : form,
        "post" : post
    }

    return render(request, "post_form.html", context)

# POSTS INDEX
def post_list(request):
    posts = Post.objects.all()
    context = {
        "titulo" : "Artículos",
        "posts" : posts 
    }
    return render(request, "index.html", context)
