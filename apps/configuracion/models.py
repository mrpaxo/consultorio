from django.db import models



#catalogos iniciales
class Medicamento(models.Model):
    descripcion = models.TextField(max_length=100)
    estado = models.BooleanField(default= True)

    def __str__(self):
        return  '%s' %  (self.descripcion)

class Enfermedad(models.Model):
    codigo = models.CharField(max_length=4)
    descripcion = models.TextField(max_length=100)
    estado = models.BooleanField(default= True)

    def __str__(self):
        return  '%s' %  (self.descripcion)
        