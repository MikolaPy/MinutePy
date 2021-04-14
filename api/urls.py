from django.urls import path

from .views import *

urlpatterns = [
    path('posts/comments/',comments),
    path('posts/',posts), #last posts in main site
    path('posts/<int:pk>/', PostDetailView.as_view()),
]
