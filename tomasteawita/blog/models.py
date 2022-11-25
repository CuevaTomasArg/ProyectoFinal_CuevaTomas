from django.db import models
from django.contrib.auth.models import User
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    perfil_image = models.ImageField(upload_to='perfil_image')
    perfil_description = models.CharField(max_length=256)
    developer_type = models.CharField(max_length=65)
    def __str__(self):
        return f'Usuario: {self.user.username}, Email: {self.user.email}'

    
class Post(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=256)
    text = models.TextField(max_length=1040, null=True, blank=True)
    image = models.ImageField(upload_to='image',null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    category = models.CharField(max_length=100)
    date = models.DateTimeField(null=True)
    def __str__(self):
        return f'Post: {self.title}'

class Comentario(models.Model):
    text = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,null=True,blank=True)
