from django.db import models

# Create your models here.


class Grupo(models.Model):
    nombre = models.CharField(max_length=64)
    estilo = models.CharField(max_length=64)
    def __str__(self):
        return self.nombre

class Musico(models.Model):
    nombre = models.CharField(max_length=64)
    instrumento = models.CharField(max_length=64)
    grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT)    
    def __str__(self):
        return self.nombre

class Concierto(models.Model):
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=64)
    grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.grupo) + " tocará en " + self.lugar + " el " + str(self.fecha)

