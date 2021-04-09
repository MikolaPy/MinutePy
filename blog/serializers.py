from rest_framework import serializers
from .models import *

class TegsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teg
        fields = ('name',)
