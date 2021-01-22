from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from django.http import HttpRequest
from django.shortcuts import render

from .forms import FormContacto

# from .models import Genero, Pelicula, Local, Cartelera, Compra
from .models import Cliente, Producto, Contacto
from django.db.models import Q

from django.http import HttpResponseRedirect

# Create your views here.

class Home(TemplateView):
    template_name = 'infomatica/index.html'

    def get_context_data(self, **kwargs):
        clientes = Cliente.objects.filter(disponible=1)
        context = super(Home, self).get_context_data(**kwargs)
        context['clientes']  = clientes
        return context

class ProductoView(TemplateView):
    template_name = 'infomatica/producto.html'

    def get_context_data(self, **kwargs):
        productos = Producto.objects.filter(disponible=1)
        context = super(ProductoView, self).get_context_data(**kwargs)
        context['productos']  = productos
        return context

class Cart(TemplateView):
    template_name = 'infomatica/cart.html'

class FormContactoView(HttpRequest):

    def index(request):
        contacto = FormContacto()
        return render(request, "infomatica/contacto.html", {"form" : contacto})
    
    def process_form(request):
        contacto = FormContacto(request.POST)
        if contacto.is_valid():
            contacto.save()
            contacto = FormContacto()
        return render(request, "infomatica/contacto.html", {"form" : contacto, "mensaje" : "OK"})



