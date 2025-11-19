from django.shortcuts import render

from rest_framework import viewsets
from .models import Content
from .serializer import ContentSerializer

# Create your views here.
class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer 