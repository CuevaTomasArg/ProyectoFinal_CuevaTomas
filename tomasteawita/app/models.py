from django.db import models

class User(models.Model):
    user_name= models.CharField(max_length=100)
    email = models.EmailField(max_length=126)
    password = models.CharField(max_length=256)
    perfil_image = models.ImageField()
    perfil_description = models.CharField(max_length=256)
    developer_type = models.CharField(max_length=65)

class Post(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=256)
    image = models.ImageField()
    user = models.CharField(max_length=100)
    id_user = models.IntegerField()
    category = models.CharField(max_length=100)

class Visit(models.Model):
    email = models.EmailField()
    developer_type = models.CharField(max_length=65)