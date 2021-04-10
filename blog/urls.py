from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import *

urlpatterns = [
    path('api/post/<int:pk>/',api_post_detail),
    path('api/tegs/',api_tegs),
    
    path('accounts/login/',BBLoginView.as_view(),name='login'),
    path('accounts/logout/',LogoutView.as_view(),name='logout'),
    path('accounts/profile/',profile,name='profile'),
    path('accounts/profile/edit/',EditUserView.as_view(),name='edit_user'),

    path('post/create/',PostCreateView.as_view(),name='postcreate'),
    path('',AllPostView.as_view(),name='main'),
    path('tegs/<str:teg_name>/',PostByTegView.as_view(),name='by_teg'),

    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='postdelete'),
    path('post/<int:pk>/edit/',PostEditView.as_view(),name='postedit'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='postdetail'),
    path('tegs/',tegs_edit,name='tegs_edit')
    ]
