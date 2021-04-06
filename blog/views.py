from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import *
from .forms import PostForm


def index(request):
    posts = Post.objects.all()
    tegs = Teg.objects.all()
    context = {'posts':posts,'tegs':tegs}
    return render(request, 'blog/main.html',context)


class PostByTegView(ListView):
    template_name = 'blog/main.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.filter(tegs__name=self.kwargs['teg_pk'])


class PostDetailView(DetailView):
    model = Post



class PostCreateView(CreateView):
    template_name = 'blog/post_create.html'
    form_class = PostForm
    success_url = reverse_lazy('main')



