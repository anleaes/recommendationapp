from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField('Nome', max_length=50)
    email = models.EmailField('E-mail',null=False, blank=False)
    ra = models.CharField('RA',null=False, blank=False,max_length=50)

    class Meta:
        verbose_name = 'Estudante'
        verbose_name_plural = 'Estudantes'
        ordering =['id']

    def __str__(self):
        return self.name
