from django.urls import path
from .views import 

urlpatterns = [
    path('ma/', MarketPageView.as_view(), name="market"),
    path('mc/', MCPageView.as_view(), name="mc")
]