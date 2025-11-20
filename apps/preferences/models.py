from django.db import models
from students.models import Student
# Create your models here

class Preference(models.Model):
    q1 = models.CharField('Como você se sente ao estudar por longos períodos?', max_length=20, default='a', choices=[
        ('1', 'Perco o foco facilmente.'),
        ('2', 'Consigo manter o foco se fizer pausas curtas.'),
        ('3', 'Prefiro estudar por blocos longos e sem interrupções.'),
        ('4', 'Gosto de revisar o conteúdo várias vezes em períodos diferentes.'),
    ])
    q2 = models.CharField('Qual formato de aprendizado você prefere?', max_length=20, default='a', choices=[
        ('1', 'Assistir vídeos ou ouvir explicações.'),
        ('2', 'Ler e fazer anotações.'),
        ('3', 'Explicar o conteúdo para alguém (ou para mim mesmo).'),
        ('4', 'Usar diagramas, esquemas ou mapas mentais.'),
    ])
    q3 = models.CharField('O que mais atrapalha seus estudos?', max_length=20, default='a', choices=[
        ('1', 'Falta de concentração.'),
        ('2', 'Dificuldade em lembrar o que estudei.'),
        ('3', 'Falta de motivação.'),
        ('4', 'Bagunça nas anotações e falta de organização.'),
    ])
  
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  
 