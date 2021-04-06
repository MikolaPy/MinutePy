from django.urls import path

from .views import * 

urlpatterns = [
    path('create/',PostCreateView.as_view(),name='create'),
    path('',AllPostView.as_view(),name='main'),
    path('<str:teg_name>/',PostByTegView.as_view(),name='by_teg'),
    path('post/<int:pk>/edit/',PostEdit.as_view(),name='editpost'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='postdetail'),
    ]
