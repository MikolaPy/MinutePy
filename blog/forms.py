from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from .models import *



class PostForm(forms.ModelForm):
    title = forms.CharField(label='Subject')
    content = forms.CharField(label='bodypost',widget=forms.widgets.Textarea(),required=False)
    tegs = forms.ModelMultipleChoiceField(queryset=Teg.objects.all(),label='teg',widget=forms.widgets.CheckboxSelectMultiple(attrs={'size':10}))
    def clean(self):
        super().clean()
        errors = {}
        if not self.cleaned_data['content']:
            errors['content'] = ValidationError('WTF there data?')
        if errors:
            raise ValidationError(errors)

    class Meta:
        model = Post
        fields = ('title','content','tegs')



class UserForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             label='email address')

    class Meta:
        model = AdvUser
        fields = ('username','email','first_name','last_name','send_message')


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(label="adress email",required=True)
    password1 = forms.CharField(label="first password",
                                widget=forms.PasswordInput,
                                #all password requirements 
                               help_text=password_validation.password_validators_help_text_html())  
    password2 = forms.CharField(label="second passwor",
                                     widget=forms.PasswordInput,
                                     help_text="input password again")


    def clean_password_first(self):
        password = self.cleaned_data['password1']
        if password:
            password_validation.validate_password(password)
        return password

    def clean(self):        
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2 :
            error = {'password':ValidationError('password missmatch')}
            raise ValidationError(error)

    def save(self,commit=True):                             #when saving new user
        user = super().save(commit=False)                      # dont save in model 
        user.set_password(self.cleaned_data['password1'])      #encoding password 
        user.is_active = False                              #cant log in yet
        user.is_activated = False
        if commit:
            user.save()
        user_register.send(RegisterUserForm,instance=user)      #sending sign
        return user                             #to send user an email requistion activation
    class Meta:
        model = AdvUser
        fields = ('username','first_name','last_name','password1','password2','email','send_message')
