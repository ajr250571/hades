from django.db import models

# Create your models here.
from datetime import datetime


class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre")

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        ordering = ["id"]

    def __str__(self):
        return self.name


class Employee(models.Model):
    names = models.CharField(max_length=150, verbose_name="Nombres")
    dni = models.CharField(max_length=10, verbose_name="DNI", unique=True)
    date_joined = models.DateField(
        default=datetime.now, verbose_name="Fecha Registro")
    date_created = models.DateTimeField(
        auto_now=True, verbose_name="Fecha Creacion")
    date_updated = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha Actualizacion")
    age = models.PositiveIntegerField(default=0, verbose_name="Edad")
    salary = models.DecimalField(
        max_digits=14, decimal_places=2, default=0.00, verbose_name="Sueldo")
    state = models.BooleanField(default=True, verbose_name="Estado")
    avatar = models.ImageField(
        upload_to="avatar/%Y/%m/%d", null=True, blank=True)
    cvitae = models.FileField(
        upload_to="cvitae/%Y/%m/%d", null=True, blank=True)
    type = models.ForeignKey(Type, verbose_name="Tipo",
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ["id"]

    def __str__(self):
        return self.names
