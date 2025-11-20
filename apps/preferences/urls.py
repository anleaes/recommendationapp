from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'preferences'

router = routers.DefaultRouter()
router.register('', views.PreferenceViewSet, basename='preferences')

urlpatterns = [
    path('', include(router.urls)),
]



