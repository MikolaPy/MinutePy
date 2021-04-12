from django.db import models
from django.contrib.auth.models import AbstractUser

# auth_model_user in setting for access setting
class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True,db_index=True)
    send_message = models.BooleanField(default=True,verbose_name="comment message")
    class Meta(AbstractUser.Meta):
        pass


class Post(models.Model):
    title = models.CharField(max_length = 50,verbose_name='sobject',blank=True)
    content = models.TextField(blank=True,null=True,verbose_name='text')
    published = models.DateTimeField(auto_now_add=True,db_index=True,verbose_name='date')
    marker = models.ManyToManyField('Marker')

    class Meta:
        unique_together = ('title','content')   #unique title + contetn
        default_related_name = 'posts'          #include post_set in Manager
        verbose_name_plural = 'Posts'
        verbose_name = 'Post'
        ordering = ['-published']
    def __str__(self):
        return self.title



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
    objects = MarkerManager
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
