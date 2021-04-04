from django.urls import path

from .views import * 

urlpatterns = [
    path('create/',PostCreateView.as_view(),name='create'),
    path('',index,name='main'),
    path('<str:teg_name>/',by_teg,name='by_teg'),
    ]
