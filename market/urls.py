from django.urls import path
from .views import MCPageView, FinancPageView, marketPageView

urlpatterns = [
    path('mc/', MCPageView.as_view(), name="mc"),
    path('financiamiento', FinancPageView.as_view(), name="financiamiento"),
    path('market/', marketPageView.as_view(), name="market"),
]

