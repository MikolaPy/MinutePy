from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import *
from .forms import PostForm
from django.urls import reverse_lazy


def index(request):
    posts = Post.objects.all()          
    tegs = Teg.objects.all()
    context = {'posts':posts,'tegs':tegs}
    return render(request, 'blog/main.html',context)


def by_teg(requst,teg_name):
    teg = Teg.objects.get(name = teg_name)
    allposts = teg.posts.all()
    return render(requst, 'blog/main.html',{'posts':allposts})

class PostCreateView(CreateView):
    template_name = 'blog/post_create.html'
    form_class = PostForm
    success_url = reverse_lazy('main')



