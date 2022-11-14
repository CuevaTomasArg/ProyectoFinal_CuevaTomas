from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def create(request):
    return render(request, 'createposrt.html')

def lobby(request):
    return render(request, 'lobby.html')
