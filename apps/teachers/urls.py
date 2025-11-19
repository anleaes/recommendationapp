from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'teachers'

router = routers.DefaultRouter()
router.register('', views.TeacherViewSet, basename='teachers')

urlpatterns = [
    path('', include(router.urls) )
]

# Na raiz do projeto acesse o arquivo "urls.py" 
# Adicione o caminho da entidade após "path('admin/', admin.site.urls),".

path('teachers/', include('teachers.urls', namespace='teachers')),

# Altere a linha de import "from django.urls import path" adicionando o include

from django.urls import path, include
