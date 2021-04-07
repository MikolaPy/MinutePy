from django import forms

from .models import *

class PostForm(forms.ModelForm):
    title = forms.CharField(label='Subject')
    content = forms.CharField(label='bodypost',widget=forms.widgets.Textarea())
    tegs = forms.ModelMultipleChoiceField(queryset=Teg.objects.all(),label='teg',widget=forms.widgets.CheckboxSelectMultiple(attrs={'size':10}))

    class Meta:
        model = Post
        fields = ('title','content','tegs')

