from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'students'

router = routers.DefaultRouter()
router.register('', views.StudentViewSet, basename='estudantes')

urlpatterns = [
    path('', include(router.urls) )
]