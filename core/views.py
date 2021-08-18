from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

class HomePageView(TemplateView):
    template_name = "core/home.html"


class NosotrosPageView(TemplateView):
    template_name = "core/nosotros.html"

class TyCPageView(TemplateView):
    template_name = "core/tyC.html"
    
class ContactoPageView(TemplateView):
    template_name = "core/contacto.html"    

# class FriendPageView(TemplateView):
#     template_name = "core/friends.html"  
def send_email(request):
    name = request.POST.get('nombre', '')
    lastname = request.POST.get('apellidos', '')
    message = request.POST.get('message', '')
    startup = request.POST.get('startup', '')
    from_email = request.POST.get('email', '')
    print(name)
    print(lastname)
    print(message)
    message = """
           Correo: {}
            StartUp{}
            {}
    """.format(from_email,startup,message)
    print(message)
    print(type(name))
    print(from_email)
    subject = name+' '+lastname
    print(subject)
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['contacto@makingfriends.com.mx'])
            print('Enviado')
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
    return render(request, 'core/friends.html', {'form': 'form'})
    # else:
    #     # In reality we'd use a form class
    #     # to get proper validation errors.
    #     return HttpResponse('Make sure all fields are entered and valid.')

class PrivacidadPageView(TemplateView):
    template_name = "core/privacidad.html"   
