from django.db import models


class Participantes(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    


