from django.db.models import Q
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.core.signing import  BadSignature

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin

from django.forms import modelformset_factory

from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test,login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib import messages


from .models import *
from .forms import *
from .utilities import signer

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
        tegs = Marker.objects.all()
        serializer = MarkersSerializer(tegs,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def api_post_detail(request,pk):
    if request.method == 'GET':
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


###########################################################################################
# AUTH
############################################################################################

# Login page
class BBLoginView(LoginView):
    template_name = 'registration/login.html'
# Profile page
@login_required
def profile(request):
    return render(request,'registration/profile.html')

# Change password page
class BBPasswordChangeView(SuccessMessageMixin,LoginRequiredMixin,PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('main')
    success_message = 'Success done ! Password change'

# Edit profile page 
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


class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('register_done')

class RegisterDoneView(TemplateView):
    template_name = 'registration/register_done.html'

def user_activate(request,sign):
    #get the identifier with the sign URl parameter
    #next extract the username and display a page 
    #with message about successful activation
    try:
        username = signer.unsign(sign)
    except BadSignature:  #if digital sign is bad ,display another page
        return render(request,'registration/bad_signature.html')
    user = get_object_or_404(AdvUser,username=username)
    if user.is_activated:  #elif user allready activated
        template = 'registration/user_is_activated.html'
    else:
        template = 'registration/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request,template)


class DeleteUserView(LoginRequiredMixin,DeleteView):
    model = AdvUser
    template_name = 'registration/delete_user.html'
    success_url = reverse_lazy('main')

    def setup(self,request,*args,**kargs):
        #save id user from requst
        self.user_id = request.user.pk
        return super().setup(request,*args,**kargs)

    def post(self,request,*args,**kargs):
        #logout from site profile via built-in function
        logout(request)
        #message successful delete user
        messages.add_message(request,messages.SUCCESS,'user delete')
        return super().post(request,*args,**kargs)
    def get_object(self,queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset,pk=self.user_id)


#######################################################################


class AllPostView(ListView):
    paginate_by = 4
    context_object_name = 'posts'
    model = Post    #all posts in object_list attr , template post_list.html


class PostByMarkerView(ListView):
    # all posts related with select marker and form search 
    
    template_name = 'blog/posts_by_teg.html'
    context_object_name = 'posts'
    paginate_by = 4

    def setup(self,request,*args,**kargs):
        self.requist = request
        return super().setup(request,*args,**kargs)

    def get_queryset(self):
        posts = Post.objects.filter(markers__name=self.kwargs['marker_name'])
        if 'key' in self.request.GET:
            self.key = self.request.GET['key']
            q = Q(title__icontains=self.key)|Q(content__icontains=self.key)
            posts = posts.filter(q)
        else:
            self.key= ''
        return posts

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        marker = Marker.objects.get(name=self.kwargs['marker_name'])
        context['marker'] = marker
        context['form'] =  SearchForm(initial={'key':self.key})
        return context


def post_detail(request,pk):
    post = Post.objects.get(pk=pk) 
    attachments = post.attachments.all()
    context = {'post':post,'attachments':attachments}
    return render(request,'blog/post_detail.html',context)


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
    MarkersFormSet = modelformset_factory(Marker,fields=('name',),
                                       can_delete=True)
    if request.method == 'POST':
        formset = MarkersFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('main')
    else:
        formset = MarkersFormSet()
    context = {'formset':formset}
    return render(request,'blog/tegs_edit.html',context)
