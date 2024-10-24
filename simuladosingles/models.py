from django.db import models

# Create your models here.
class Question(models.Model):
    pergunta = models.CharField(max_length=200)
    assertiva1 = models.CharField(max_length=200)
    assertiva2 = models.CharField(max_length=200)
    assertiva3 = models.CharField(max_length=200)
    assertiva4 = models.CharField(max_length=200)
    resposta = models.IntegerField()
