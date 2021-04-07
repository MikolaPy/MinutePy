from django.urls import path

from .views import * 

urlpatterns = [
    path('post/create/',PostCreateView.as_view(),name='postcreate'),
    path('',AllPostView.as_view(),name='main'),
    path('tegs/',tegs_edit,name='tegs_edit'),
    path('<str:teg_name>/',PostByTegView.as_view(),name='by_teg'),

    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='postdelete'),
    path('post/<int:pk>/edit/',PostEditView.as_view(),name='postedit'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='postdetail'),
    ]
