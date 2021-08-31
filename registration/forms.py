from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 carácteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nombre', 'apellido', 'fecha', 'genero']
        # widgets = {
        #     'nombre': forms.TextInput(attrs={'class':'col-md-6'}),
        #     'apellido': forms.TextInput(attrs={'class':'col-md-6'}),
        #     'fecha': forms.DateInput(attrs={'class':'col-md-6','type':"date"}),
        #     'direcccion': forms.Textarea(attrs={'class':'col-md-6','rows': 4}),
        # }



