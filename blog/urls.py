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
    path('accounts/password/change/',BBPasswordChangeView.as_view(),name='password_change'),
    path('accounts/register/',RegisterUserView.as_view(),name='register'),
    path('accounts/register/done/',RegisterDoneView.as_view(),name='register_done'),
    path('accounts/register/activate/<str:sign>/',user_activate,name='register_activate'),
    path('accounts/delete/',DeleteUserView.as_view(),name='delete_user'),

    path('',AllPostView.as_view(),name='main'),
    path('marker/<str:marker_name>/',PostByMarkerView.as_view(),name='by_marker'),
    #path('tegs/',tegs_edit,name='tegs_edit'),

    path('post/create/',post_create,name='postcreate'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='postdelete'),
    path('post/<int:pk>/edit/',post_edit,name='postedit'),
    path('post/<int:pk>/',post_detail,name='postdetail'),
    ]
