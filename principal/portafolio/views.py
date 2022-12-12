from django.shortcuts import render
from django.views.generic.list import ListView
from portafolio.models import Usuario, Proyecto

# Create your views here.  
class ProyectoList(ListView):
    model = Proyecto
    template_name = "portafolio.html"