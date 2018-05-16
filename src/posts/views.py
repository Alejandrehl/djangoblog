from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def post_create(request):
    return HttpResponse("<h1>Create post</h1>")

def post_detail(request):
    return HttpResponse("<h1>Post detail</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete post</h1>")

def post_update(request):
    return HttpResponse("<h1>Update post</h1>")

def post_list(request):
    return HttpResponse("<h1>Posts lists</h1>")
