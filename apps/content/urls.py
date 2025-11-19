from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'content'

router = routers.DefaultRouter()
router.register('', views.ContentViewSet, basename='conteúdo')

urlpatterns = [
    path('', include(router.urls) )
]