from django import forms
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm

class Post_user_form(forms.Form):
    user_name= forms.CharField(max_length=100)
    email = forms.EmailField(max_length=126)
    password = forms.CharField(max_length=256)
    perfil_image = forms.ImageField()
    perfil_description = forms.CharField(max_length=256)
    developer_type = forms.CharField(max_length=65)

class Post_post_form(forms.Form):
    title = forms.CharField(max_length=75)
    description = forms.CharField(max_length=256)
    image = forms.ImageField()
    user = forms.CharField(max_length=100)
    category = forms.CharField(max_length=100)

class Post_visit_form(forms.Form):
    email = forms.EmailField()
    developer_type = forms.CharField(max_length=65)
    
class SingUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]