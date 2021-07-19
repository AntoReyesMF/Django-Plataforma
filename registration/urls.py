from django.urls import path
from .views import SingUpView, preferenciasView, perfilView, perfil2View

urlpatterns = [
    
    path('signup/' ,SingUpView.as_view(), name ='signup'),
    #path('login/' , login_request, name ='login'),
    #path("logout", logout_request, name= "logout"),
    # path('profile/', ProfileUpdate.as_view(), name="profile"),
    path('preferencias/' , preferenciasView.as_view(), name ='preferencias'),
    path('perfil/' , perfilView.as_view(), name ='perfil'),
    path('perfil2/' , perfil2View.as_view(), name ='perfil2'),
]
