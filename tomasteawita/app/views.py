from django.shortcuts import render
from django.http import HttpResponse
from .forms import * #Post_post_form, Post_user_form, Post_visit_form
from .models import *
# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html',context=context)

def search(request):
    if request.GET.get('title', False):
        title = request.GET['title']
        post = Post.objects.filter(title__icontains=title)

        return render(request, 'buscar_profesor.html', {'post': post})
    else:
        respuesta = 'No hay datos'
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'search.html', context = context)

def create_post(request):
    if request.method == 'POST':
        form = Post_post_form(request.POST)
        if form.is_valid():
            form_cleaned = form.cleaned_data
            post = Post(title = form_cleaned['title'],description = form_cleaned['description'],image = form_cleaned['image'],user = form_cleaned['user'],category = form_cleaned['category'])
            post.save()
        else:
            return render(request, 'index.html')
        return render(request,'checkPostCreate.html')
    else:
        form = Post_post_form()
    return render(request, 'createpost.html',{'form': form})

def lobby(request):
    if request.method == 'POST':
        form = Post_user_form(request.POST)
        if form.is_valid():
            form_cleaned = form.cleaned_data
            user = User(user_name = form_cleaned['user_name'],email = form_cleaned['email'],password = form_cleaned['password'],perfil_image = form_cleaned['perfil_image'],perfil_description = form_cleaned['perfil_description'],developer_type = form_cleaned['developer_type'])
            user.save()
            return render(request,'checkPostCreate.html')
    else:
            form = Post_user_form()
    return render(request, 'userPost.html')

def checkPostCreate(request):
    return render(request, 'checkPostCreate.html')
