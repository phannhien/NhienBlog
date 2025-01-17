from django.db import models

# Create your models here.
class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)