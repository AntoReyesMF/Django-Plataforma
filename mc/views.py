from django.shortcuts import render
from django.views.generic.base import TemplateView 

# Create your views here.

class colePageView(TemplateView):
    template_name = 'mc/colectivo.html'

class cole1PageView(TemplateView):
    template_name = 'mc/colectivo_1.html'

class cole2PageView(TemplateView):
    template_name = 'mc/colectivo_2.html'

class cole3PageView(TemplateView):
    template_name = 'mc/colectivo_3.html'

class cole4PageView(TemplateView):
    template_name = 'mc/colectivo_4.html'

class cole5PageView(TemplateView):
    template_name = 'mc/colectivo_5.html'

class cole6PageView(TemplateView):
    template_name = 'mc/colectivo_6.html'

class cole8PageView(TemplateView):
    template_name = 'mc/colectivo_8.html'    

class coleFinalPageView(TemplateView):
    template_name = 'mc/colectivo_final.html'  

