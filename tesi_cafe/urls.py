from django.urls import path
from .views import tesi_cafePageView, tesi_cafe_inicioPageView, tesi_cafe_taller1PageView, tesi_cafe_taller2PageView, tesi_cafe_taller3PageView, tesi_cafe_taller4PageView, tesi_cafe_taller5PageView, tesi_cafe_taller6PageView, tesi_cafe_taller7PageView, tesi_cafe_taller8PageView, tesi_cafe_taller9PageView, tesi_cafe_taller10PageView, tesi_cafe_taller11PageView, tesi_cafe_taller12PageView, tesi_cafe_taller13PageView, tesi_cafe_taller14PageView

urlpatterns = [
    path('', tesi_cafePageView.as_view(), name="tesi_cafe"),
    path('tesi_cafe_inicio', tesi_cafe_inicioPageView.as_view(), name="tesi_cafe_inicio"),
    path('tesi_cafe_taller1', tesi_cafe_taller1PageView.as_view(), name="tesi_cafe_taller1"),
    path('tesi_cafe_taller2', tesi_cafe_taller2PageView.as_view(), name="tesi_cafe_taller2"),
    path('tesi_cafe_taller3', tesi_cafe_taller3PageView.as_view(), name="tesi_cafe_taller3"),
    path('tesi_cafe_taller4', tesi_cafe_taller4PageView.as_view(), name="tesi_cafe_taller4"),
    path('tesi_cafe_taller5', tesi_cafe_taller5PageView.as_view(), name="tesi_cafe_taller5"),
    path('tesi_cafe_taller6', tesi_cafe_taller6PageView.as_view(), name="tesi_cafe_taller6"),
    path('tesi_cafe_taller7', tesi_cafe_taller7PageView.as_view(), name="tesi_cafe_taller7"),
    path('tesi_cafe_taller8', tesi_cafe_taller8PageView.as_view(), name="tesi_cafe_taller8"),
    path('tesi_cafe_taller9', tesi_cafe_taller9PageView.as_view(), name="tesi_cafe_taller9"),
    path('tesi_cafe_taller10', tesi_cafe_taller10PageView.as_view(), name="tesi_cafe_taller10"),
    path('tesi_cafe_taller11', tesi_cafe_taller11PageView.as_view(), name="tesi_cafe_taller11"),
    path('tesi_cafe_taller12', tesi_cafe_taller12PageView.as_view(), name="tesi_cafe_taller12"),
    path('tesi_cafe_taller13', tesi_cafe_taller13PageView.as_view(), name="tesi_cafe_taller13"),
    path('tesi_cafe_taller14', tesi_cafe_taller14PageView.as_view(), name="tesi_cafe_taller14"),
    
]