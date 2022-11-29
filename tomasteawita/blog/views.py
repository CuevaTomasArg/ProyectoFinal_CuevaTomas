from django.shortcuts import render
from django.http import HttpResponse
from .forms import * 
from .models import *
from datetime import datetime
from django.views.generic import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required

def search(request):
    show_category = Post.objects.all()
    show_category_buttons = []
    for cat in show_category:
        if  cat.category in show_category_buttons:
            pass
        else:
            show_category_buttons.append(cat.category)
    if request.GET.get('category_id', False):
        category_id = request.GET['category_id']
        posts = Post.objects.filter(category_id=category_id)
        return render(request, 'search.html', {'posts': posts,'show_category_buttons':show_category_buttons})
    return render(request, 'search.html', {'show_category': show_category ,'show_category_buttons':show_category_buttons})

def upload_post(request):
    if request.method == 'POST':
        post = PostForm(initial={'user': request.user.pk,'date':datetime.now()},data = request.POST, files= request.FILES)
        if post.is_valid():
            post_cleaned = post.cleaned_data
            post_clean = Post(user=post_cleaned['user'],date=post_cleaned['date'],title = post_cleaned['title'],description = post_cleaned['description'],text = post_cleaned['text'],image = post_cleaned['image'],category = post_cleaned['category'])
            post_clean.save()
        return render(request,'postValid.html')
    else:
        form = PostForm(initial={'text':"Aqui va el contenido",'user': request.user.pk,'date':datetime.now()})
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


def detail_user(request,user_id):
    user = User.objects.get(id=user_id)
    posts = Post.objects.filter(user_id = user_id)
    try:
        avatar = Avatar.objects.get(user=user)
        context = {'user':user,'posts':posts,'avatar':avatar} 
    except:
        context = {'user':user,'posts':posts}
    return render(request,'detailUser.html',context=context)

def detail_post(request,post_id):
    post = Post.objects.get(id=post_id)
    context = {'post':post}
    try:
        avatar = Avatar.objects.get(user_id=post.user.id)
        context['avatar'] = avatar
    except:
        pass
    try:
        coments = Comentario.objects.filter(post_id=post_id)
        context['coments'] = coments
    except:
        pass
    if request.method == 'POST':
        coment_form = ComentForm(request.POST)
        coment_form.user = request.user.pk
        coment_form.post = post_id
        if coment_form.is_valid():
            coment_form_clean = coment_form.cleaned_data
            coment_clean = Comentario(text= coment_form_clean['text'],user = request.user,post =post)
            coment_clean.save()
    else:
        coment_form = ComentForm(initial={'user':request.user.pk,'post':post_id})
        context['form'] = coment_form
    return render(request, 'detailPost.html',context = context)
    

class Index(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'index.html'



# class detail_post(DetailView,CreateView):
#     model = Post
#     form_class = ComentForm
#     template_name = 'detailPost.html'
    
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