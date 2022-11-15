from django.conf import settings
from django.views.static import serve
from django.urls import path, re_path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('search/', search, name="search"),
    path('create_post/', create_post, name="create"),
    path('check/', checkPostCreate, name="checkPostCreate"),
    path('singin/', singin, name="sing in"),
    path('loginVisit/',loginVisit, name="loginVisit"),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$',serve,{
        'document_root': settings.MEDIA_ROOT,
    })
]


