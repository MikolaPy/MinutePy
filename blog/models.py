from django.db import models
from django.contrib.auth.models import AbstractUser

# auth_model_user in setting for access seting
class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True,db_index=True)
    send_message = models.BooleanField(default=True,verbose_name="comment message")
    class Meta(AbstractUser.Meta):
        pass



class Post(models.Model):
    title = models.CharField(max_length = 50,verbose_name='sobject',blank=True)
    content = models.TextField(blank=True,null=True,verbose_name='text')
    published = models.DateTimeField(auto_now_add=True,db_index=True,verbose_name='date')
    tegs = models.ManyToManyField('Teg')

    class Meta:
        unique_together = ('title','content')   #unique title + contetn
        default_related_name = 'posts'          #include post_set
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
