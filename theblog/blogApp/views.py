from django.shortcuts import render
from rest_framework import generics , viewsets, permissions, mixins
from rest_framework.response import Response
# Create your views here.
from .models import post
from .serializers import postSerializer
from django.shortcuts import get_object_or_404



class allPosts(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = post.objects.all()
    serializer_class = postSerializer

