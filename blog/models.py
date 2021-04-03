from django.db import models


class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField(blank=True,null=True)
    published = models.DateTimeField(auto_now_add=True,db_index=True)

