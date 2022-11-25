from django.conf import settings
from django.views.static import serve
from django.urls import path, re_path
from .views import *
from django.conf.urls.static import static
# from django.views.static import serve
# from django.conf.urls.static import static


urlpatterns = [
    path('',Index.as_view(),name="index"),
    path('detailPost/<pk>',detail_post.as_view(),name="DetailPost"),
    path('confirm_delete_post/<pk>',delete_post.as_view(),name="DeletePost"),
    path('edit_post/<pk>',EditPost.as_view(),name="EditPost"),
    path('Update_post/',UpdatePost.as_view(),name="Update Post"),
    path('SingUp/',SingUp.as_view(),name="SingUp"),
    path('login/',AdminLoginView.as_view(),name="Login"),
    path('logout/',AdminLogoutView.as_view(),name="Logout"),
    path('search/', search, name="search"),
    path('uploadPost/', upload_post, name="upload post"),
    path('valid/', post_valid, name="post_valid"),
    path('singin/', sing_in, name="sing in"),
    path('editUser/',edit_user, name="edit user"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += [
#     re_path(r'^media/(?P<path>.*)$',serve,{
#         'document_root': settings.MEDIA_ROOT,
#     })
# ]
