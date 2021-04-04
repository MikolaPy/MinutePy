from django.urls import path

from .views import index,by_teg

urlpatterns = [
    path('<str:teg_name>/',by_teg),
    path('',index),
    ]
