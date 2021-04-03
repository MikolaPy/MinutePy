from django.db import models


class Post(models.Model):
    " for setting display fields model need change par in blog/admin.py "

    title = models.CharField(max_length = 50,verbose_name='sobject')
    content = models.TextField(blank=True,null=True,verbose_name='text')
    published = models.DateTimeField(auto_now_add=True,db_index=True,
                                    verbose_name='date')

    class Meta:
        verbose_name_plural = 'Posts'
        verbose_name = 'Post'
        ordering = ['-published']

