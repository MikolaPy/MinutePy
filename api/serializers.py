from rest_framework import serializers

from blog.models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title','content','published')



class PostDetailSetializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title','content','published','image')


class CommentSerializer(serializers.ModelSerializer):
    model = Comment 
    fields = ('post','created_at','text','title','author')
