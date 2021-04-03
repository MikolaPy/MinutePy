from django.db import models 

class Post(models.Model):
    title = models.CharFiels(max_length=50)
    content = models.TextField(null=True,blank=True)
    published = models.DateTimeField(auto_now_add=True,db_index=True)

    
