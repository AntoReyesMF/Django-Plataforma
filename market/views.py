from django.shortcuts import render
from django.views.generic.base import TemplateView 


# Create your views here.
class marketPageView(TemplateView):
    template_name= "market/marketplace.html"

class MCPageView(TemplateView):
    template_name = "market/MC.html"    

class FinancPageView(TemplateView):
    template_name = "market/financiamiento.html"    



