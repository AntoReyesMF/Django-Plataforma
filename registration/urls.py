from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import UserPasswordResetForm
from .views import SingUpView, preferenciasView, perfilView, perfil2View2

urlpatterns = [
    
    path('signup/' ,SingUpView.as_view(), name ='signup'),
    #path('login/' , login_request, name ='login'),
    #path("logout", logout_request, name= "logout"),
    # path('profile/', ProfileUpdate.as_view(), name="profile"),
    path('preferencias/' , preferenciasView.as_view(), name ='preferencias'),
    path('perfil/' , perfilView.as_view(), name ='perfil'),
    #path('perfil2/' , perfil2View.as_view(), name ='perfil2'),
    path('perfil2/' , perfil2View2, name ='perfil2'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
    template_name='registration/password_reset.html',
    form_class=UserPasswordResetForm),name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
      auth_views.PasswordResetConfirmView.as_view(
      template_name='registration/password_reset_confirm.html'), 
      name='password_reset_confirm'),    
]
