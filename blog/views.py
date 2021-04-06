from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import *
from .forms import PostForm

'''
def index(request):
    posts = Post.objects.all()
    tegs = Teg.objects.all()
    context = {'posts':posts,'tegs':tegs}
    return render(request, 'blog/main.html',context)
'''


class AllPostView(ListView):
    model = Post    #all posts in object_list attr , template post_list.html
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tegs'] = Teg.objects.all()
        context['posts'] = context['object_list']
        return context




class PostByTegView(ListView):
    template_name = 'blog/posts_by_teg.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.filter(tegs__name=self.kwargs['teg_name'])
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['teg'] = Teg.objects.get(name = self.kwargs['teg_name'])
        return context


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    template_name = 'blog/post_create.html'
    form_class = PostForm
    success_url = reverse_lazy('main')



