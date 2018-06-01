from django.db import models

# Create your models here.
def upload_location(instance, filename):
    return '$s/$s' %(instance.id, filename)

class Post(models.Model):

    titulo = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    imagen = models.ImageField(null=True,
                             blank=True,
                             height_field="height_field",
                             width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    contenido = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.titulo 

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post_detail', args=[str(self.id)])

    class Meta:
        ordering = ["-timestamp", "-actualizado"]