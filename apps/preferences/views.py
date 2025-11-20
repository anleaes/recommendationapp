from django.shortcuts import render
from .models import Preference
from rest_framework import viewsets
from .serializer import PreferenceSerializer

# Após o comentario "# Create your views here." e crie as views "Product".

class PreferenceViewSet(viewsets.ModelViewSet):
    queryset = Preference.objects.all()
    serializer_class = PreferenceSerializer 