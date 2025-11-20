from django.db import models
from students.models import Student
from contents.models import Content

# Create your models here.
class Recommendation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Recomendação'
        verbose_name_plural = 'Recomendações'
        ordering =['id']

    def __str__(self):
        return self.name
