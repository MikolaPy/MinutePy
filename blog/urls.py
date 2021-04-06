from django.urls import path

from .views import * 

urlpatterns = [
    path('create/',PostCreateView.as_view(),name='create'),
    path('',index,name='main'),
    path('<str:teg_pk>/',PostByTegView.as_view(),name='by_teg'),
    path('post/<int:pk>',PostDetailView.as_view(),
         name='postdetail'),
    ]
