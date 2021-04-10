from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.core.paginator import Paginator

from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin

from django.forms import modelformset_factory
from .models import *
from .forms import *

from django.contrib.auth.decorators import user_passes_test,login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView

####################################################################
##


## API REST
from .serializers import *
#for display 
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_tegs(request):
    if request.method == 'GET':
        tegs = Teg.objects.all()
        serializer = TegsSerializer(tegs,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def api_post_detail(request,pk):
    if request.method == 'GET':
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


######################################################################
# AUTH


class BBLoginView(LoginView):
    template_name = 'registration/login.html'


@login_required
def profile(request):
    return render(request,'registration/profile.html')

class BBPasswordChangeView(SuccessMessageMixin,LoginRequiredMixin,PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('main')
    success_message = 'Success done ! Password change'

class EditUserView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model = AdvUser
    template_name = 'registration/edit_user.html'
    form_class = UserForm
    success_url = reverse_lazy('profile')
    success_message = 'Change edit'
    
    def setup(self,request,*args,**kargs): # easy way get user
        self.user_id = request.user.pk
        return super().setup(request,*args,**kargs)
    def get_object(self,queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset,pk=self.user_id)


#######################################################################


class AllPostView(ListView):
    paginate_by = 4
    context_object_name = 'posts'
    model = Post    #all posts in object_list attr , template post_list.html


class PostByTegView(ListView):
    template_name = 'blog/posts_by_teg.html'
    context_object_name = 'posts'
    paginate_by = 4
    def get_queryset(self):
        self.post_by_teg = Post.objects.filter(tegs__name=self.kwargs['teg_name'])
        return self.post_by_teg
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['teg_name']=self.kwargs['teg_name']
        return context


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    template_name = 'blog/post_create.html'
    form_class = PostForm
    def get_success_url(self):
        obj = self.object.pk
        return reverse_lazy('postdetail',kwargs = {"pk":obj})

class PostEditView(LoginRequiredMixin,UpdateView):
    teplate_name = 'blog/post_edit.html'
    model = Post
    form_class = PostForm
    def get_success_url(self):
        obj = self.object.pk
        return reverse_lazy('postdetail',kwargs = {"pk":obj})

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model= Post
    template_name_suffix = "_delete" 
    success_url = reverse_lazy('main')

@user_passes_test(lambda user : user.is_superuser)
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
