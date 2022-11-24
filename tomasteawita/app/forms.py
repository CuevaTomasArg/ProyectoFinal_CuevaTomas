from django import forms
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm
from .models import *
class Post_user_form(forms.Form):
    perfil_image = forms.ImageField()
    perfil_description = forms.CharField(max_length=1024)
    developer_type = forms.CharField(max_length=65)

class Post_post_form(forms.Form):
    title = forms.CharField(max_length=75)
    description = forms.CharField(max_length=1024)
    image = forms.ImageField()
    category = forms.CharField(max_length=100)
    
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        
class SingUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
class UserEditForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        help_texts = {k:'' for k in fields}