from django.db import models
from django.utils import timezone

#Clase de prueba. 
"""
    En esta clase se están creando el modelo de datos de un post 
    que tiene un autor, titulo, texto posteado y fecha de publicación

"""
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title