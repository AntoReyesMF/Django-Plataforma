from django.urls import path
from .views import mi_cochinito_basePageView, mi_cochinito_inicioPageView, mi_cochinito_taller1PageView, mi_cochinito_taller2PageView, mi_cochinito_taller3PageView, mi_cochinito_taller4PageView, mi_cochinito_taller5PageView, mi_cochinito_taller6PageView, mi_cochinito_taller7PageView, mi_cochinito_taller8PageView, mi_cochinito_taller9PageView

urlpatterns = [
    path('', mi_cochinito_inicioPageView.as_view(), name="mi_cochinito_inicio"),
    path('mi_cochinito_taller1', mi_cochinito_taller1PageView.as_view(), name="mi_cochinito_taller1"),
    path('mi_cochinito_taller2', mi_cochinito_taller2PageView.as_view(), name="mi_cochinito_taller2"),
    path('mi_cochinito_taller3', mi_cochinito_taller3PageView.as_view(), name="mi_cochinito_taller3"),
    path('mi_cochinito_taller4', mi_cochinito_taller4PageView.as_view(), name="mi_cochinito_taller4"),
    path('mi_cochinito_taller5', mi_cochinito_taller5PageView.as_view(), name="mi_cochinito_taller5"),
    path('mi_cochinito_taller6', mi_cochinito_taller6PageView.as_view(), name="mi_cochinito_taller6"),
    path('mi_cochinito_taller7', mi_cochinito_taller7PageView.as_view(), name="mi_cochinito_taller7"),
    path('mi_cochinito_taller8', mi_cochinito_taller8PageView.as_view(), name="mi_cochinito_taller8"),
    path('mi_cochinito_taller9', mi_cochinito_taller9PageView.as_view(), name="mi_cochinito_taller9"),
]

