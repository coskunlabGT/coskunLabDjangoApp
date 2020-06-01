from django.http import JsonResponse
from django.shortcuts import render
from django.http import Http404
from rest_framework import status

# third party imports
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import PostSerializer
from .models import Post

def getAllObjects():
    return Post.objects.all()

def getObject(pk):
    return Post.objects.get(id = pk)


