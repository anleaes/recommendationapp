from django.shortcuts import render
from .models import Recommendation
from rest_framework import viewsets
from .serializer import RecommendationSerializer

# Create your views here.
class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer  