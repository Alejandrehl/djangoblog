from django.contrib import admin
from .models import Post

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["titulo", "actualizado","timestamp"]
    list_display_links = ["actualizado"]
    list_filter = ["timestamp"]
    search_fields = ["titulo", "contenido"]
    list_editable = ["titulo"]
    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
