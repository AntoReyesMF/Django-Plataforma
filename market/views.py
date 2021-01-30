from django.shortcuts import render
from django.views.generic.base import TemplateView 


# Create your views here.
class MarketPageView(TemplateView):
    
    template_name= "market/marketplace.html"

class MCPageView(TemplateView):
    template_name = "market/MC.html"    



