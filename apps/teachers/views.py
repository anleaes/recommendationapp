from django.shortcuts import render
from .models import Teacher
from rest_framework import viewsets
from .serializer import TeacherSerializer

# Após o comentario "# Create your views here." e crie as views "Product".

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer 