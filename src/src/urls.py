from django.contrib import admin
from django.urls import path

from posts.views import post_list
from posts.views import post_create
from posts.views import post_detail
from posts.views import post_delete
from posts.views import post_update

urlpatterns = [
    path('admin/', admin.site.urls),

    path('posts/', post_list, name="post_list"),
    path('posts/create', post_create, name="post_create"),
    path('posts/detail', post_detail, name="post_create"),
    path('posts/delete', post_delete, name="post_create"),
    path('posts/update', post_update, name="post_create"),
]