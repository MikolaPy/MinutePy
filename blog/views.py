from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from django.shortcuts import render 
from .models import Post

def index(request):
    posts = Post.objects.all()          
    context = {'posts':posts}
    return render(request, 'blog/main.html',context)
