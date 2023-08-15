from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'servicio'

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.TextField(max_length=200)
    telefono = models.IntegerField()
    ubicacion = models.PointField()
    servicio = models.ForeignKey(Servicio,on_delete=models.CASCADE)
    
    class Meta:
        managed = True
        db_table = 'cliente'

