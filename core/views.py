from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = "core/home.html"


class NosotrosPageView(TemplateView):
    template_name = "core/nosotros.html"

class TyCPageView(TemplateView):
    template_name = "core/tyC.html"
    
class ContactoPageView(TemplateView):
    template_name = "core/contacto.html"    

class FriendPageView(TemplateView):
    template_name = "core/friends.html"    
