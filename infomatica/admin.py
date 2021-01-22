from django.contrib import admin
from .models import Cliente, Producto, Contacto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'producto', 'precio', 'disponible']

admin.site.register(Producto, ProductoAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'empresa', 'nombre_cliente', 'disponible']

admin.site.register(Cliente, ClienteAdmin)

class ContactoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'empresa', 'telefono', 'correo']

admin.site.register(Contacto, ContactoAdmin)