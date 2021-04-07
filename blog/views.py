from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.forms import modelformset_factory
from .models import *
from .forms import PostForm

"""
def index(request):
    posts = Post.objects.all()
    tegs = Teg.objects.all()
    context = {'posts':posts,'tegs':tegs}
    return render(request, 'blog/main.html',context)
"""

class AllPostView(ListView):
    paginate_by = 4
    context_object_name = 'posts'
    model = Post    #all posts in object_list attr , template post_list.html


class PostByTegView(ListView):
    template_name = 'blog/posts_by_teg.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.filter(tegs__name=self.kwargs['teg_name'])
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['teg_name']=self.kwargs['teg_name']
        return context


class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    template_name = 'blog/post_create.html'
    form_class = PostForm
    def get_success_url(self):
        obj = self.object.pk
        return reverse_lazy('postdetail',kwargs = {"pk":obj})

class PostEditView(UpdateView):
    teplate_name = 'blog/post_edit.html'
    model = Post
    form_class = PostForm
    def get_success_url(self):
        obj = self.object.pk
        return reverse_lazy('postdetail',kwargs = {"pk":obj})

class PostDeleteView(DeleteView):
    model= Post
    template_name_suffix = "_delete" 
    success_url = reverse_lazy('main')

def tegs_edit(request):
    TegsFormSet = modelformset_factory(Teg,fields=('name',),
                                       can_delete=True)
    if request.method == 'POST':
        formset = TegsFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('main')
    else:
        formset = TegsFormSet()
    context = {'formset':formset}
    return render(request,'blog/tegs_edit.html',context)
