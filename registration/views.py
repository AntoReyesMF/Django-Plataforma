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
from django.urls import reverse_lazy
from django import forms
from .forms import UserCreationFormWithEmail, ProfileForm
from .models import Profile

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


def login_request(request):
    if request.method == "POST":
        print(request.POST.get('submit'))
        print(request.POST)
        if request.POST.get('submit') == 'Acceder':
            print(request.POST.get('submit'))
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect("perfil")
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")
        if request.POST.get('submit') == 'signup':
            forms = UserCreationFormWithEmail(request.POST)
            if forms.is_valid():
                forms.save()
                username = forms.cleaned_data.get('username')
                raw_password = forms.cleaned_data.get('password')
                user = authenticate(username=username, password=raw_password)
                login(request, user,backend='django.contrib.auth.backends.ModelBackend')
                return redirect('login')
            else:
                form = UserCreationFormWithEmail()

    form = UserCreationFormWithEmail()

    return render(request=request, template_name="registration/login.html",context={"form": form})# context={"form": form}


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")
# def registration(request):
# 	#if request.method == 'POST':
# 	return render(request, 'registration/registro.html')


class preferenciasView(TemplateView):
    template_name = "registration/preferencias.html"


class perfilView(TemplateView):
    template_name = "registration/perfil.html"


class perfil2View(TemplateView):
    template_name = "registration/perfil2.html"
