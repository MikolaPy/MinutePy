from django.urls import path

from .views import * 

urlpatterns = [
    path('create/',PostCreateView.as_view(),name='create'),
    path('',index,name='main'),
    path('<str:teg_name>/',PostByTegView.as_view(),name='by_teg'),
    ]
