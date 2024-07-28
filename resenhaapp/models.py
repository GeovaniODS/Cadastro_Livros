from django.db import models

# Create your models here.
class leituras(models.Model):
    nomelivro = models.TextField(max_length=255)
    lido = models.BooleanField(default=False)
    resenha = models.TextField()