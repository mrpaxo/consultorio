from django.db import models

# Create your models here.

STATUS =((1,'Activo'),
(2,'Cancelado'),
(3,'No Asistio'),)

COLOR = (
    ('#fcf12e','Amarillo'),
    ('#ff0000','Rojo'),
    ('#5fb5f3','Azul'),
    ('#51ee4d','Verde'),
    
    
)
class Cita(models.Model):

    paciente = models.ForeignKey('persona.Paciente', on_delete=models.CASCADE)
    inicio = models.DateTimeField()
    observacion = models.TextField(max_length = 500, blank= True, null = True)
    color = models.CharField('Color',choices = COLOR, max_length = 50, default='#51ee4d')
    status = models.PositiveSmallIntegerField('Estado',choices = STATUS, default = 1)
    
    def __str__(self):
        return '%s' % (self.pk)