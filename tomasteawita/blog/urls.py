from django.conf import settings
from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('',Index.as_view(),name="index"),
    path('detailPost/<int:post_id>',detail_post,name="DetailPost"),
    path('detailUser/<int:user_id>',detail_user,name="DetailUser"),
    path('confirm_delete_post/<pk>',delete_post.as_view(),name="DeletePost"),
    path('edit_post/<pk>',EditPost.as_view(),name="EditPost"),
    path('Update_post/',UpdatePost.as_view(),name="Update Post"),
    path('SingUp/',SingUp.as_view(),name="SingUp"),
    path('login/',AdminLoginView.as_view(),name="Login"),
    path('logout/',AdminLogoutView.as_view(),name="Logout"),
    path('search/', search, name="search"),
    path('uploadPost/', upload_post, name="upload post"),
    path('valid/', post_valid, name="post_valid"),
    path('editUser/',edit_user, name="edit user"),
    path('editAvatar/',edit_avatar, name='edit avatar'),
    path('createAvatar/',create_avatar, name='create avatar')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
