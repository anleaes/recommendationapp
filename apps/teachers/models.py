from django.db import models


# Create your models here.

class Teacher(models.Model):
    name = models.CharField('Nome', max_length=50)
    email = models.EmailField('E-mail',null=False, blank=False) 
    area = models.CharField('Area', max_length=20, default='andamento', choices=[
        ('saude', 'Saúde'),
        ('educacao', 'Educação'),
        ('tecnologia', 'Tecnologia'),
        ('direito', 'Direito'),
    ])
   

    class Meta:
        verbose_name = 'Teachers'
        verbose_name_plural = 'Teachers'
        ordering =['id']

    def __str__(self):
        return self.name