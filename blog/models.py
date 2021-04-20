from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from django.contrib.contenttypes.models import ContentType
from .utilities import *
from django.db import models
from django.contrib.auth.models import AbstractUser

# auth_model_user in setting for access setting
class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True,db_index=True)
    send_message = models.BooleanField(default=True,verbose_name="comment message")
    class Meta(AbstractUser.Meta):
        pass

    def delete(self,*args,**kargs):
    #delete all uset posts 
        for post in self.posts.all():
            post.delete()
        super().delete(*args,**kargs)


class Post(models.Model):
    title = models.CharField(max_length = 50,verbose_name='sobject',blank=True)
    content = models.TextField(blank=True,null=True,verbose_name='text')
    published = models.DateTimeField(auto_now_add=True,db_index=True,verbose_name='date')
    markers = models.ManyToManyField('Marker')
    image = models.ImageField(blank=True,upload_to=create_filename,
                               verbose_name='main_images')
    author = models.ForeignKey(AdvUser,on_delete=models.CASCADE,
                               verbose_name='post author')
    likes = GenericRelation('Like')

    def delete(self,*args,**kargs):
        #when post delete we delete related record in investmant model from db
        for im in self.attachments.all():
            im.delete()
        super().delete(*args,**kargs)

    class Meta:
        unique_together = ('title','content')   #unique title + contetn
        default_related_name = 'posts'          #include post_set in Manager
        verbose_name_plural = 'Posts'
        verbose_name = 'Post'
        ordering = ['-published']
        abstract = False

    def __str__(self):
        return self.title


class News(Post):
    markers = None

class Attachment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name='attachments')
    image = models.ImageField(upload_to=create_filename,verbose_name='image')

    class Meta:
        default_related_name = 'attachments'    #include post_set in Manager
        verbose_name_plural='attacments'
        verbose_name = 'attacment'


class Like(models.Model):
    user = models.OneToOneField(AdvUser,on_delete=models.CASCADE,verbose_name="user")
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    like_object = GenericForeignKey(ct_field="content_type",fk_field="object_id")

    class Meta:
        verbose_name = "like"
        verbose_name_plural = "likes"
        unique_together = ("user","object_id")


class Comment(models.Model):
    author = models.CharField(max_length=30,verbose_name='nickname')
    title = models.CharField(max_length=30,verbose_name='subject')
    text = models.TextField(verbose_name='text')
    created_at = models.DateTimeField(auto_now_add=True,db_index=True,verbose_name='created at')
    likes = GenericRelation("Like")
    parent = models.ForeignKey('self',on_delete=models.SET_NULL,verbose_name='parant comment',
                       blank=True,null=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name='post')

    class Meta:
        default_related_name = 'comments'
        unique_together =  ('author','text','post')
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        ordering = ['created_at']

###############################################################################################
#
#       SECTIONS
#   One post may have many markers , marker have one main section.
#   Admin can create and edit all section on one page in admine site. ?admin.py for detail?
#   User can create new marker. 
#   Marker must have main section.
#
#*****************************************************************************************
class Section(models.Model):
    name = models.CharField(max_length=20,db_index=True,unique=True,
                            verbose_name='section name')
    order = models.IntegerField(default=0,db_index=True,verbose_name='order')
    main_section = models.ForeignKey('MainSection',on_delete=models.PROTECT,null=True,
                                     blank=True,verbose_name='main section')
    def __str__(self):
        return self.name


class MarkerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(main_section__isnull=False)

class Marker(Section):
    objects = MarkerManager()
    class Meta:
        proxy = True
        ordering = ('main_section__order','main_section__name','order','name')
        verbose_name = 'marler'
        verbose_name_plural = 'markers'


class MainSectionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(main_section__isnull=True) 

class MainSection(Section):
    objects = MainSectionManager() #new manager
    class Meta:
        proxy = True
        ordering = ('order','name')
        verbose_name = 'MainSection'
        verbose_name_plural = 'MainSections'
