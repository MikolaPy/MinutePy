from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from .models import *
from .forms import PostForm


def index(request):
    posts = Post.objects.all()
    tegs = Teg.objects.all()
    context = {'posts':posts,'tegs':tegs}
    return render(request, 'blog/main.html',context)


class PostByTegView(TemplateView):
    template_name = 'blog/main.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(
            tegs__name=context["teg_name"])
        return context


class PostDetailView(DetailView):
    model = Post



class PostCreateView(CreateView):
    template_name = 'blog/post_create.html'
    form_class = PostForm
    success_url = reverse_lazy('main')



