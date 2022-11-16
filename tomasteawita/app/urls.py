from django.conf import settings
from django.views.static import serve
from django.urls import path, re_path
from .views import *
from django.conf.urls.static import static
# from django.views.static import serve
# from django.conf.urls.static import static


urlpatterns = [
    path('',index,name="index"),
    path('search/', search, name="search"),
    path('uploadPost/', upload_post, name="Upload post"),
    path('check/', checkPostCreate, name="checkPostCreate"),
    path('singin/', singin, name="sing in"),
    path('loginVisit/',loginVisit, name="loginVisit"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += [
#     re_path(r'^media/(?P<path>.*)$',serve,{
#         'document_root': settings.MEDIA_ROOT,
#     })
# ]
