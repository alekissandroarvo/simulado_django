from django.db import models

# Create your models here.
class Question(models.Model):
    pergunta = models.CharField(max_length=500)
    assertiva1 = models.CharField(max_length=500)
    assertiva2 = models.CharField(max_length=500)
    assertiva3 = models.CharField(max_length=500)
    assertiva4 = models.CharField(max_length=500)
    resposta = models.CharField(max_length=500)

class FillInBlank(models.Model):
    pergunta = models.CharField(max_length=5000)
    resposta = models.CharField(max_length=5000)

class FillInBlank_by_topic(models.Model):
    assunto=models.CharField(max_length=500)
    pergunta = models.CharField(max_length=5000)
    resposta = models.CharField(max_length=5000)

class Question_by_topic(models.Model):
    assunto=models.CharField(max_length=500)
    pergunta = models.CharField(max_length=500)
    assertiva1 = models.CharField(max_length=500)
    assertiva2 = models.CharField(max_length=500)
    assertiva3 = models.CharField(max_length=500)
    assertiva4 = models.CharField(max_length=500)
    resposta = models.CharField(max_length=500)
