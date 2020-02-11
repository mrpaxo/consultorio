from django.db import models
from django.contrib.auth.models import User
# Create your models here.
    
class RecetaDescripcion(models.Model):
    medicamento = models.ForeignKey('configuracion.Medicamento',on_delete = models.CASCADE)
    indicacion = models.TextField(max_length = 300)
    def __str__(self):
        return  '%s' %  (self.id)

class Receta(models.Model):
    doctor = models.ForeignKey(User ,blank = True, null = True, on_delete=models.CASCADE)
    descripcion = models.ManyToManyField(RecetaDescripcion, blank= True)
    
    def __str__(self):
        return  '%s' %  (self.id)


class Consulta(models.Model):
    paciente = models.ForeignKey('persona.Paciente', on_delete=models.CASCADE)
    peso = models.PositiveSmallIntegerField()
    talla = models.PositiveSmallIntegerField()
    estatura = models.DecimalField(max_digits=3, decimal_places=2)
    motivo = models.TextField(max_length=500, blank = True, null = True)
    examen_fisico = models.TextField(max_length=500 ,blank = True, null = True)
    examen_laboratorio = models.TextField(max_length=500,blank = True, null = True)
    diagnostico = models.TextField(max_length=500,blank = True, null = True)
    receta = models.ForeignKey(Receta,on_delete=models.CASCADE, blank = True, null = True )
    estado = models.BooleanField(default = True)

    def paciente_fullname(self):
        return '%s  %s  %s' % (self.paciente.nombre, self.paciente.ap_paterno, self.paciente.ap_materno)
    def __str__(self):
        return  '%s' %  (self.id)