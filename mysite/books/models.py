from django.db import models

# Create your models here.
class Permisos(models.Model):
    codPermiso=models.AutoField('ID', primary_key=True)
    nombre=models.CharField(max_length=200)
    observacion=models.CharField(max_length=200,null=True, blank=True)

    def _unicode_(self):
        return u"%s the place" % self.nombre




class Rol(models.Model):
    codRol=models.AutoField('ID', primary_key=True)
    nombre=models.CharField(max_length=200)
    observacion=models.CharField(max_length=200)
    #permisos




class Usuario(models.Model):
    codUsuario=models.AutoField('ID', primary_key=True)
    nombre=models.CharField(max_length=200)
    contrasenha=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    nroDocumento=models.CharField(max_length=200)
    estado=models.CharField(max_length=1)
    fkrol=models.ForeignKey(Rol)

    def _unicode_(self):
        return u"%s probar %s" % (self.fkrol, self.nombre)



