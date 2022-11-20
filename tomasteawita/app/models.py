from django.db import models

class Usuario(models.Model):
    user_name= models.CharField(max_length=100)
    email = models.EmailField(max_length=126)
    password = models.CharField(max_length=256)
    perfil_image = models.ImageField(upload_to='perfil_image')
    perfil_description = models.CharField(max_length=256)
    developer_type = models.CharField(max_length=65)
    def __str__(self):
        return f'Usuario: {self.user_name}, Email: {self.email}'

class Post(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=256)
    image = models.ImageField(upload_to='image')
    user = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    def __str__(self):
        return f'Post: {self.title}'

class Visit(models.Model):
    email = models.EmailField()
    developer_type = models.CharField(max_length=65)
    def __str__(self):
        return f'Visit: {self.email}, Developer:{self.developer_type}'

class Comentario(models.Model):
    text = models.CharField(max_length=256)
    autor = models.CharField(max_length=100)
