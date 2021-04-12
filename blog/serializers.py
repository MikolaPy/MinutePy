from rest_framework import serializers
from .models import *

class TegsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marker
        fields = ('name',)
        


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ('title','content','published')
