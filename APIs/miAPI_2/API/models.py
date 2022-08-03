from django.db import models

# Create your models here.

class Employee(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    direccion= models.CharField(max_length=100)
    email= models.EmailField()
    salario= models.IntegerField()
