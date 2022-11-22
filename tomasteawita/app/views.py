from django.shortcuts import render
from django.http import HttpResponse
from .forms import * 
from .models import *
from django.views.generic import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
#Los decoradores sirven para vistas  basadas en cñases
from django.contrib.auth.decorators import login_required
#los mixins sirven para vistas basadas en classes
from django.contrib.auth.mixins import LoginRequiredMixin

#Lo que hace este login es que evita que yo pueda acceder a ciertos campos si yo no estoy logeado
#Pero esto me da un error 404, para corregir esto hay que ir a settings.py a hacer una configuracion para que en vez de que me de error, me envie
#Al login u otra parte de la pagina. Sigue el omentario en el settings.py ->


@login_required

def search(request):
    show_category = Post.objects.all()
    show_category_buttons = []
    for cat in show_category:
        if  cat.category in show_category_buttons:
            pass
        else:
            show_category_buttons.append(cat.category)
    if request.GET.get('category', False):
        category = request.GET['category']
        posts = Post.objects.filter(category__icontains=category)

        return render(request, 'search.html', {'posts': posts,'show_category_buttons':show_category_buttons})
    return render(request, 'search.html', {'show_category': show_category ,'show_category_buttons':show_category_buttons})

def upload_post(request):
    if request.method == 'POST':
        post = Post_post_form(data = request.POST, files= request.FILES)
        if post.is_valid():
            post_cleaned = post.cleaned_data
            post_limpio = Post(title = post_cleaned['title'],description = post_cleaned['description'],image = post_cleaned['image'],user = post_cleaned['user'],category = post_cleaned['category'])
            post_limpio.save()
        return render(request,'postValid.html')
    else:
        form = Post_post_form()
    return render(request, 'uploadPost.html',{'form': form})

def sing_in(request):
    if request.method == 'POST':
        form = Post_user_form(data = request.POST, files= request.FILES)
        if form.is_valid():
            form_cleaned = form.cleaned_data
            user = Usuario(user_name = form_cleaned['user_name'],email = form_cleaned['email'],password = form_cleaned['password'],perfil_image = form_cleaned['perfil_image'],perfil_description = form_cleaned['perfil_description'],developer_type = form_cleaned['developer_type'])
            user.save()
            return render(request,'postValid.html')
    else:
        form = Post_user_form()
    return render(request, 'singin.html',{'form': form})

def login_visit(request):
    if request.method == 'POST':
        form = Post_visit_form(request.POST)
        if form.is_valid():
            form_cleaned = form.cleaned_data
            visit = Visit(email = form_cleaned['email'],developer_type = form_cleaned['developer_type'])
            visit.save()
            return render(request,'postValid.html')
    else:
        form = Post_visit_form()
    return render(request, 'loginVisit.html',{'form': form})

def post_valid(request):
    return render(request, 'postValid.html')




class Index(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'index.html'

class detail_post(DetailView):
    model = Post
    template_name = 'detailPost.html'
    
class delete_post(DeleteView):
    model = Post
    success_url = '/'
    template_name = 'confirm_post_delete.html'
    
class EditPost(UpdateView):
    model = Post
    success_url = '/'
    template_name = 'edit_post.html'
    fields = ['title','description','image','user','category']
    
class UpdatePost(CreateView):
    model = Post
    success_url = '/'
    template_name = 'edit_post.html'
    fields = ['title','description','image','user','category']
    
class SingUp(CreateView):
    form_class = SingUpForm
    success_url = reverse_lazy('index')
    template_name = 'singup.html'

class AdminLoginView(LoginView):
    template_name = 'login.html'
    
class AdminLogoutView(LogoutView):
    template_name = 'logout.html'