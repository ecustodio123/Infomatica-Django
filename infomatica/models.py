from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):
    
    STATUS = (
        (0, 'No Disponible'),
        (1, 'Disponible')
    )

    id = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to='images/posts', max_length=255, blank=True, null=True)
    velocidad = models.CharField(max_length=255, blank=False, null=False)
    precio = models.CharField(max_length=10, blank=False, null=False)
    certificado = models.IntegerField(default=1, choices=STATUS)
    disponible = models.IntegerField(default=1, choices=STATUS)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']
        indexes = [
            models.Index(fields=['producto', 'velocidad', 'precio', 'certificado', 'disponible'])
        ]
    
    def __str__(self):
        return self.producto

class Cliente(models.Model):
    
    STATUS = (
        (0, 'No Disponible'),
        (1, 'Disponible')
    )

    id = models.AutoField(primary_key=True)
    empresa = models.CharField(max_length=255, blank=False, null=False)
    nombre_cliente = models.CharField(max_length=255, blank=False, null=False)
    cargo = models.CharField(max_length=255, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='images/posts', max_length=255, blank=True, null=True)
    disponible = models.IntegerField(default=1, choices=STATUS)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']
        indexes = [
            models.Index(fields=['empresa', 'nombre_cliente', 'cargo', 'disponible'])
        ]
    
    def __str__(self):
        return self.empresa


class Contacto(models.Model):
 
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=False, null=False)
    telefono = models.CharField(max_length=25, blank=False, null=False)
    correo = models.CharField(max_length=150, blank=False, null=False)
    empresa = models.CharField(max_length=150, blank=False, null=False)
    identificacion = models.CharField(max_length=150, blank=False, null=False)
    metodoContacto = models.CharField(max_length=150, blank=False, null=False)
    mensaje = models.TextField(blank=False, null=False)
    date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        ordering = ['id']
        indexes = [
            models.Index(fields=['nombre', 'empresa', 'telefono', 'correo'])
        ]
    
    def __str__(self):
        return self.nombre