from django.urls import path
from .views import vexi_inicioPageView, vexi_taller1PageView, vexi_taller2PageView, vexi_taller3PageView, vexi_taller4PageView, vexi_taller5PageView, vexi_taller6PageView, vexi_taller7PageView, vexi_taller8PageView, vexi_taller9PageView, vexi_taller10PageView, vexi_taller11PageView, vexi_taller12PageView, vexi_taller13PageView, vexi_edufinPageView

urlpatterns = [
    path('', vexi_inicioPageView.as_view(), name="vexi_inicio"),
    path('vexi_edufin', vexi_edufinPageView.as_view(), name="vexi_edufin"),
    path('vexi_taller1', vexi_taller1PageView.as_view(), name="vexi_taller1"),
    path('vexi_taller2', vexi_taller2PageView.as_view(), name="vexi_taller2"),
    path('vexi_taller3', vexi_taller3PageView.as_view(), name="vexi_taller3"),
    path('vexi_taller4', vexi_taller4PageView.as_view(), name="vexi_taller4"),
    path('vexi_taller5', vexi_taller5PageView.as_view(), name="vexi_taller5"),
    path('vexi_taller6', vexi_taller6PageView.as_view(), name="vexi_taller6"),
    path('vexi_taller7', vexi_taller7PageView.as_view(), name="vexi_taller7"),
    path('vexi_taller8', vexi_taller8PageView.as_view(), name="vexi_taller8"),
    path('vexi_taller9', vexi_taller9PageView.as_view(), name="vexi_taller9"),
    path('vexi_taller10', vexi_taller10PageView.as_view(), name="vexi_taller10"),
    path('vexi_taller11', vexi_taller11PageView.as_view(), name="vexi_taller11"),
    path('vexi_taller12', vexi_taller12PageView.as_view(), name="vexi_taller12"),
    path('vexi_taller13', vexi_taller13PageView.as_view(), name="vexi_taller13"),
    
    
]




