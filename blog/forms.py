from django import forms
from django.core.exceptions import ValidationError 
from .models import *

class PostForm(forms.ModelForm):
    title = forms.CharField(label='Subject')
    content = forms.CharField(label='bodypost',widget=forms.widgets.Textarea(),required=False)
    tegs = forms.ModelMultipleChoiceField(queryset=Teg.objects.all(),label='teg',widget=forms.widgets.CheckboxSelectMultiple(attrs={'size':10}))
    def clean(self):
        super().clean()
        errors = {}
        if not self.cleaned_data['content']:
            errors['content'] = ValidationError('WTF')
        if errors:
            raise ValidationError(errors)

    class Meta:
        model = Post
        fields = ('title','content','tegs')

