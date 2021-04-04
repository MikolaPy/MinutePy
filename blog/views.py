from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from django.shortcuts import render 
from .models import Post,Teg

def index(request):
    posts = Post.objects.all()          
    context = {'posts':posts}
    return render(request, 'blog/main.html',context)


def teg_post_view(requst,teg_name):
    teg = Teg.objects.get(name = teg_name)
    allposts = teg.posts.all() 
    return render(requst, 'blog/main.html',{'posts':allposts})
