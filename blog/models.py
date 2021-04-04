from django.db import models
from django.contrib.auth.models import User

" for register and setting display fields model need change options in blog/admin.py "

class AdvUser(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)



class Post(models.Model):
    title = models.CharField(max_length = 50,verbose_name='sobject',blank=True)
    content = models.TextField(blank=True,null=True,verbose_name='text')
    published = models.DateTimeField(auto_now_add=True,db_index=True,verbose_name='date')
    tegs = models.ManyToManyField('Teg')


    default_related_name = 'posts' 
    unique_together = ('title','content')
    

    class Meta:
        verbose_name_plural = 'Posts'
        verbose_name = 'Post'
        ordering = ['-published']
        
    def __str__(self):
        return self.title



class Teg(models.Model):
    name = models.CharField(max_length= 40,unique=True,
                            verbose_name = 'teg_name')

    class Meta:
        verbose_name_plural = 'tegs'
        verbose_name = 'teg'
        ordering = ['name']
    def __str__(self):
        return self.name
