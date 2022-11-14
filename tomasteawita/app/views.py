from django.shortcuts import render
from .forms import Post_post_form, Post_user_form, Post_visit_form
from .models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def create_post(request):
    if request.method == 'POST':
        form = Post_post_form(request.POST)
        if form.is_valid():
            user = User.objects.filter(id__icontains = form.user)
            form_cleaned = form.cleaned_data
            post = Post(title = form_cleaned['title'],description = form_cleaned['description'],image = form_cleaned['image'],user = form_cleaned['user'],id_user = user)
            post.save()
            return render(request,'checkPostCreate.html')
        else:
            form = Post_post_form()
    return render(request, 'createpost.html',{'form': form})

def lobby(request):
    return render(request, 'lobby.html')

def checkPostCreate(request):
    return render(request, 'checkPostCreate.html')
