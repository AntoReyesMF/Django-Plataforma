from django.urls import path
from .views import SingUpView, ProfileUpdate,preferenciasView, perfilView

urlpatterns = [
    
    path('signup/' ,SingUpView.as_view(), name ='signup'),
    path('profile/', ProfileUpdate.as_view(), name="profile"),
    path('preferencias/' , preferenciasView.as_view(), name ='preferencias'),
    path('perfil/' , perfilView.as_view(), name ='perfil'),
]
