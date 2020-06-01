from rest_framework import serializers

from .models import Post
from django import forms

# transformation from model to json
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'