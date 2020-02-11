from django.db import models

# Create your models here.
SEXO = (
    ('M','Masculino'),
    ('F','Femenino'),
)

class BasePersona(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    ap_paterno = models.CharField('Apellido Paterno', max_length=50)
    ap_materno = models.CharField('Apellido Materno', max_length=50)
    sexo = models.CharField('Sexo',choices = SEXO, max_length = 10, default='M')
    domicilio = models.CharField('Domicilio', max_length=300)
    telefono = models.CharField('Telefono', max_length=15)
    celular = models.CharField('Celular', max_length=15, null=True, blank=True)
    fech_nac = models.DateField('Fecha Nacimiento')
    email = models.EmailField('Email', max_length=50, null=True, blank=True)


    def __str__(self):
        return '%s - %s - %s' % (self.nombre, self.ap_paterno, self.ap_materno)


class Paciente(BasePersona):
    nom_responsable = models.CharField('Persona Responsable', max_length=100),
    estado = models.BooleanField(default=True)

