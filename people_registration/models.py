from django.db import models

class Pessoa(models.Model):
    person_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome
    