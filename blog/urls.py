from django.urls import path

from .views import index 

urlpattern = [
    path('',index),
    ]
