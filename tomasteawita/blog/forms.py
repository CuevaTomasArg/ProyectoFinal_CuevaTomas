from django import forms
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm
from .models import *
class Post_user_form(forms.Form):
    perfil_image = forms.ImageField()
    perfil_description = forms.CharField(max_length=1024)
    developer_type = forms.CharField(max_length=65)
    

class ComentForm(forms.Form):
    text = forms.CharField(max_length=256)
    user = forms.ModelChoiceField(queryset=User.objects.all())
    post = forms.ModelChoiceField(queryset=Post.objects.all())

class PostForm(forms.Form):
    title = forms.CharField(max_length=75)
    description = forms.CharField(max_length=256)
    text = forms.CharField(max_length=1040)
    image = forms.ImageField()
    user = forms.ModelChoiceField(queryset=User.objects.all())
    category = forms.ModelChoiceField(queryset=Category.objects.all())    
    date = forms.DateTimeField()
        
class SingUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        help_texts = {k:'' for k in fields}


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