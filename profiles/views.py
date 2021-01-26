from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.

class preferenciasView(TemplateView):
    template_name = "profiles/preferencias.html"
   
class perfilView(TemplateView):
    template_name = "profiles/perfil.html"