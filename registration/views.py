from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django import forms
from .forms import UserCreationFormWithEmail, ProfileForm
from .models import Profile ,Profile_Portada
from django.db.models import F

# Create your views here.


class SingUpView(CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?registrer'

    def get_form(self, form_class=None):
        form = super(SingUpView, self).get_form()
        # Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(
            attrs={'class': 'col-md-6', 'placeholder': 'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'col-md-6', 'placeholder': 'Dirección email'})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'col-md-6', 'placeholder': 'Contraseñaa'})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'col-md-6', 'placeholder': 'Repite la contraseña'})
        return form


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('perfil')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        # recuperar el objeto que se va editar
        profile, created = Profile.objects.get_or_create(
            user=self.request.user)
        return profile


# def logout_request(request):
#     logout(request)
#     messages.info(request, "You have successfully logged out.")
#     return redirect("home")
# # def registration(request):
# # 	#if request.method == 'POST':
# # 	return render(request, 'registration/registro.html')


class preferenciasView(TemplateView):
    template_name = "registration/preferencias.html"


class perfilView(TemplateView):
    template_name = "registration/perfil.html"


def perfil2View2(request):
    portadas = Profile_Portada.objects.get(user_id=request.user) 
    if request.method == "POST":
        if request.POST.get('usernamet'):
            print(request.POST.get('usernamet'))
            owner = request.user
            print(request)
            print(owner)
            owner.username = request.POST.get('usernamet')
            owner.save()   
            #savest = 
            return render(request,'registration/perfil2.html') 
        if request.POST.get('nombre'):
            form = ProfileForm(request.POST)
            pro = Profile.objects.all()  
            print(request.POST.get('nombre'))
            print(request.POST.get('fecha'))
            print(form)
            if form.is_valid():  
                try:  
                    profile, created = Profile.objects.get_or_create(
                                user=request.user)
                    print(profile)     
                    profile.nombre = request.POST.get('nombre')
                    profile.apellido = request.POST.get('apellido')
                    profile.fecha = request.POST.get('fecha')
                    profile.genero = request.POST.get('genero')
                    profile.save()
                    #form.save()  
                    render(request,'registration/perfil2.html',{'pro':pro})  
                except:  
                    print('No pude jeje')
        ###portada            
        if request.POST.get('luna'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('luna'))
            try:
                profileportada, created = Profile_Portada.objects.get_or_create(
                                    user=request.user)
                print(profileportada) 
                profileportada.direct_imgs3 = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/img/Karma_0.jpg'#request.POST.get('luna')
                profileportada.save()    
                #savest = 
                return render(request,'registration/perfil2.html')             
            except:  
                    print('No pude jeje')
            #savem =
            
    else:
        return render(request,'registration/perfil2.html',{'portadas':portadas})         


# class perfil2View(TemplateView):
#     template_name = "registration/perfil2.html"


