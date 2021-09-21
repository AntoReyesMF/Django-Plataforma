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
from time import sleep

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
    try:
        portadas = Profile_Portada.objects.get(user_id=request.user) 
    except:
        portadas = 0

    print(portadas)
    if request.method == "POST":
        if request.POST.get('usernamet'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('usernamet'))
            owner = request.user
            print(request)
            print(owner)
            owner.username = request.POST.get('usernamet')
            owner.save()   
            portadas = Profile_Portada.objects.get(user_id=request.user) 
            #savest = 
            return render(request,'registration/perfil2.html',{'portadas':portadas})
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
        ###
        ###         
        if request.POST.get('perfil2_F1'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil2_F1'))
            try:
                profileportada, created = Profile_Portada.objects.get_or_create(
                                    user=request.user)
                print(profileportada) 
                profileportada.direct_imgs3 = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/portada/f1.png'#request.POST.get('luna')
                profileportada.save()   
                
                portadas = Profile_Portada.objects.get(user_id=request.user) 
                #savest = 
                return render(request,'registration/perfil2.html',{'portadas':portadas})             
            except:  
                    print('No pude jeje')

        if request.POST.get('perfil2_F2'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil2_F2'))
            try:
                profileportada, created = Profile_Portada.objects.get_or_create(
                                    user=request.user)
                print(profileportada) 
                profileportada.direct_imgs3 = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/portada/f2.jpg'#request.POST.get('luna')
                profileportada.save()   
                
                portadas = Profile_Portada.objects.get(user_id=request.user) 
                #savest = 
                return render(request,'registration/perfil2.html',{'portadas':portadas})             
            except:  
                    print('No pude jeje')

        if request.POST.get('perfil2_F3'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil2_F3'))
            try:
                profileportada, created = Profile_Portada.objects.get_or_create(
                                    user=request.user)
                print(profileportada) 
                profileportada.direct_imgs3 = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/portada/f3.jpg'#request.POST.get('luna')
                profileportada.save()   
                
                portadas = Profile_Portada.objects.get(user_id=request.user) 
                #savest = 
                return render(request,'registration/perfil2.html',{'portadas':portadas})             
            except:  
                    print('No pude jeje')
        if request.POST.get('perfil2_F4'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil2_F4'))
            try:
                profileportada, created = Profile_Portada.objects.get_or_create(
                                    user=request.user)
                print(profileportada) 
                profileportada.direct_imgs3 = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/portada/f4.jpg'#request.POST.get('luna')
                profileportada.save()   
                
                portadas = Profile_Portada.objects.get(user_id=request.user) 
                #savest = 
                return render(request,'registration/perfil2.html',{'portadas':portadas})             
            except:  
                    print('No pude jeje')
        if request.POST.get('perfil2_F5'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil2_F5'))
            try:
                profileportada, created = Profile_Portada.objects.get_or_create(
                                    user=request.user)
                print(profileportada) 
                profileportada.direct_imgs3 = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/portada/f5.jpg'#request.POST.get('luna')
                profileportada.save()   
                
                portadas = Profile_Portada.objects.get(user_id=request.user) 
                #savest = 
                return render(request,'registration/perfil2.html',{'portadas':portadas})             
            except:  
                    print('No pude jeje')
        if request.POST.get('perfil2_F6'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil2_F6'))
            try:
                profileportada, created = Profile_Portada.objects.get_or_create(
                                    user=request.user)
                print(profileportada) 
                profileportada.direct_imgs3 = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/portada/f6.jpg'#request.POST.get('luna')
                profileportada.save()   
                
                portadas = Profile_Portada.objects.get(user_id=request.user) 
                #savest = 
                return render(request,'registration/perfil2.html',{'portadas':portadas})             
            except:  
                    print('No pude jeje')
        if request.POST.get('perfil2_F7'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil2_F7'))
            try:
                profileportada, created = Profile_Portada.objects.get_or_create(
                                    user=request.user)
                print(profileportada) 
                profileportada.direct_imgs3 = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/portada/f7.jpg'#request.POST.get('luna')
                profileportada.save()   
                
                portadas = Profile_Portada.objects.get(user_id=request.user) 
                #savest = 
                return render(request,'registration/perfil2.html',{'portadas':portadas})             
            except:  
                    print('No pude jeje')
        if request.POST.get('perfil2_F8'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil2_F8'))
            try:
                profileportada, created = Profile_Portada.objects.get_or_create(
                                    user=request.user)
                print(profileportada) 
                profileportada.direct_imgs3 = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/portada/f8.jpg'#request.POST.get('luna')
                profileportada.save()   
                
                portadas = Profile_Portada.objects.get(user_id=request.user) 
                #savest = 
                return render(request,'registration/perfil2.html',{'portadas':portadas})             
            except:  
                    print('No pude jeje')
        if request.POST.get('perfil2_F9'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil2_F9'))
            try:
                profileportada, created = Profile_Portada.objects.get_or_create(
                                    user=request.user)
                print(profileportada) 
                profileportada.direct_imgs3 = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/portada/f9.jpg'#request.POST.get('luna')
                profileportada.save()   
                
                portadas = Profile_Portada.objects.get(user_id=request.user) 
                #savest = 
                return render(request,'registration/perfil2.html',{'portadas':portadas})             
            except:  
                    print('No pude jeje')
        if request.POST.get('perfil2_F10'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil2_F10'))
            try:
                profileportada, created = Profile_Portada.objects.get_or_create(
                                    user=request.user)
                print(profileportada) 
                profileportada.direct_imgs3 = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/portada/f10.jpg'#request.POST.get('luna')
                profileportada.save()   
                
                portadas = Profile_Portada.objects.get(user_id=request.user) 
                #savest = 
                return render(request,'registration/perfil2.html',{'portadas':portadas})             
            except:  
                    print('No pude jeje')

        #
        #
        #
        #### FOTOS DE PERFIL
        # 
        # 
        #          
        if request.POST.get('perfil2_Pp1'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil2_Pp1'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p1.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')  

        if request.POST.get('perfil_Pp2'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp2'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p2.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')

        if request.POST.get('perfil_Pp3'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp3'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p3.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')

        if request.POST.get('perfil_Pp4'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp4'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p4.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje') 

        if request.POST.get('perfil_Pp5'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp5'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p5.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')

        if request.POST.get('perfil_Pp6'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp6'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p6.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')

        if request.POST.get('perfil_Pp7'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp7'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p7.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje') 

        if request.POST.get('perfil_Pp8'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp8'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p8.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')

        if request.POST.get('perfil_Pp9'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp9'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p9.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')  

        if request.POST.get('perfil_Pp10'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp10'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p10.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')

        if request.POST.get('perfil2_Pp11'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil2_Pp11'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p11.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')

        if request.POST.get('perfil_Pp12'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp12'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p12.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje') 

        if request.POST.get('perfil_Pp13'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp13'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p13.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')

        if request.POST.get('perfil_Pp14'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp14'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p14.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')

        if request.POST.get('perfil_Pp15'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp15'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p15.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje') 

        if request.POST.get('perfil_Pp16'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp16'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p16.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')  

        if request.POST.get('perfil_Pp17'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp17'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p17.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')  

        if request.POST.get('perfil_Pp18'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp18'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p18.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')

        if request.POST.get('perfil_Pp19'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp19'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p19.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')

        if request.POST.get('perfil_Pp20'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp20'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p20.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje') 

        if request.POST.get('perfil2_Pp21'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil2_Pp21'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p21.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')

        if request.POST.get('perfil_Pp22'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp22'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p22.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')

        if request.POST.get('perfil_Pp23'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp23'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p23.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje') 

        if request.POST.get('perfil_Pp24'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp24'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p24.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')   

        if request.POST.get('perfil_Pp25'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp25'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p25.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')  

        if request.POST.get('perfil_Pp26'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp26'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p26.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')

        if request.POST.get('perfil_Pp27'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp27'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p27.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')

        if request.POST.get('perfil_Pp28'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp28'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p28.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje') 

        if request.POST.get('perfil_Pp29'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp29'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p29.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')

        if request.POST.get('perfil_Pp30'):
            form = Profile_Portada(request.POST)
            print(request.POST.get('perfil_Pp30'))
            try:
                 profileportada, created = Profile_Portada.objects.get_or_create(
                                     user=request.user)
                 print(profileportada) 
                 profileportada.profile_photo = 'https://makingfriedsimgpublic.s3.us-west-1.amazonaws.com/usuarios/perfil/p30.jpg'#request.POST.get('luna')
                 profileportada.save()    
                 portadas = Profile_Portada.objects.get(user_id=request.user) 
                 #savest = 
                 return render(request,'registration/perfil2.html',{'portadas':portadas})               
            except:  
                     print('No pude jeje')

                                 
            
    else:
        return render(request,'registration/perfil2.html',{'portadas':portadas})         

# class perfil2View(TemplateView):
#     template_name = "registration/perfil2.html"


