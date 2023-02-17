from django.db import models

# Create your models here.

class Usuarios(models.Model):
   nombre=models.CharField(max_length=30)
   email=models.EmailField()
   tfno = models.CharField(max_length=10, blank=True,null=True)
   descripcion=models.CharField(max_length=150)
   
   def __str__(self):
       return self.nombre

class Categorias(models.Model):
    desarrollo=models.CharField(max_length=150)
    investigacion=models.CharField(max_length=150)
   
    def __str__(self):
       return self.desarrollo