from django.urls import path
from .views import MarketPageView

urlpatterns = [
    path('ma/', MarketPageView.as_view(), name="market"),
]