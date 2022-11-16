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
    if request.GET.get('category', False):
        category = request.GET['category']
        posts = Post.objects.filter(category__icontains=category)

        return render(request, 'search.html', {'posts': posts})
    else:
        respuesta = 'No hay datos'
    return render(request, 'search.html', {'respuesta':respuesta})

def upload_post(request):
    if request.method == 'POST':
        post = Post_post_form(data = request.POST, files= request.FILES)
        if post.is_valid():
            post_cleaned = post.cleaned_data
            post_limpio = Post(title = post_cleaned['title'],description = post_cleaned['description'],image = post_cleaned['image'],user = post_cleaned['user'],category = post_cleaned['category'])
            post_limpio.save()
        return render(request,'checkPostCreate.html')
    else:
        form = Post_post_form()
    return render(request, 'uploadPost.html',{'form': form})

def singin(request):
    if request.method == 'POST':
        form = Post_user_form(data = request.POST, files= request.FILES)
        if form.is_valid():
            form_cleaned = form.cleaned_data
            user = User(user_name = form_cleaned['user_name'],email = form_cleaned['email'],password = form_cleaned['password'],perfil_image = form_cleaned['perfil_image'],perfil_description = form_cleaned['perfil_description'],developer_type = form_cleaned['developer_type'])
            user.save()
            return render(request,'checkPostCreate.html')
    else:
        form = Post_user_form()
    return render(request, 'singin.html',{'form': form})

def loginVisit(request):
    if request.method == 'POST':
        form = Post_visit_form(request.POST)
        if form.is_valid():
            form_cleaned = form.cleaned_data
            visit = Visit(email = form_cleaned['email'],developer_type = form_cleaned['developer_type'])
            visit.save()
            return render(request,'checkPostCreate.html')
    else:
        form = Post_visit_form()
    return render(request, 'loginVisit.html',{'form': form})

def checkPostCreate(request):
    return render(request, 'checkPostCreate.html')
