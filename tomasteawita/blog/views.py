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
            # post_limpio = Post(user = user,title = post_cleaned['title'],description = post_cleaned['description'],image = post_cleaned['image'],category = post_cleaned['category'])
            # post_limpio.save()
        return render(request,'postValid.html')
    else:
        form = Post_post_form()
    return render(request, 'uploadPost.html',{'form': form})

def post_valid(request):
    return render(request, 'postValid.html')

def edit_user(request):
    user = request.user
    if request.method == 'POST':
        user_form = UserEditForm(request.POST)
        if user_form.is_valid():
            information = user_form.cleaned_data
            user.username = information['username']
            user.email = information['email']
            user.password1 = information['password1']
            user.password2 = information['password2']
            user.save()
            return render(request,'index.html',{'user': user})
            
    else:
        user_form = UserEditForm(initial={'username': user.username,'email': user.email})
            
    return render(request,'editUser.html',{
        'form': user_form,
        'user': user
    })

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
    fields = ['title','description','image','category','avatar']
    
    

class SingUp(CreateView):
    form_class = SingUpForm
    success_url = '/'
    template_name = 'singup.html'

class AdminLoginView(LoginView):
    template_name = 'login.html'
    
class AdminLogoutView(LogoutView):
    template_name = 'logout.html'