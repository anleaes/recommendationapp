from django.db import models
from categories.models import Category
from teachers.models import Teacher

# Create your models here.
class Content(models.Model):
    title = models.CharField('Título', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    url = models.CharField('URL', max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Conteúdo'
        verbose_name_plural = 'Conteúdos'
        ordering =['id']

    def __str__(self):
        return self.title